#!/usr/bin/env python3
import os, json, subprocess, tempfile, shutil

ROOT = os.path.dirname(os.path.dirname(__file__))
FACTS_DIR = os.path.join(ROOT, 'assets', 'facts')
OUT_DIR = os.path.join(ROOT, 'assets', 'tts')

# Configure voices (can be overridden via env)
VOICE_EN = os.environ.get('VM_TTS_VOICE_EN', 'Samantha')
VOICE_TH = os.environ.get('VM_TTS_VOICE_TH', 'Kanya')

def choose_voice(pref_name, lang_hint):
    try:
        out = subprocess.check_output(['say', '-v', '?'], text=True)
    except Exception:
        return pref_name
    voices = []
    for line in out.splitlines():
        parts = line.split()
        if len(parts) < 2:
            continue
        name = parts[0]
        lang = parts[1]
        voices.append((name, lang))
    names = {n for n,_ in voices}
    if pref_name in names:
        return pref_name
    # try any voice that matches language code (e.g., 'th_' or 'en_')
    for n,l in voices:
        if l.lower().startswith(lang_hint.lower()):
            return n
    # fallback: first available voice
    return voices[0][0] if voices else pref_name

def ensure_dir(p):
    os.makedirs(p, exist_ok=True)

def say_to_m4a(text, voice, out_path):
    tmpdir = tempfile.mkdtemp(prefix='vmtts_')
    tmp_m4a = os.path.join(tmpdir, 'tmp.m4a')
    try:
        # Try direct M4A from say (newer macOS)
        cmd = ['say', '-v', voice, '-o', tmp_m4a, '--file-format=m4af', '--data-format=aac', text]
        res = subprocess.run(cmd)
        if res.returncode == 0 and os.path.exists(tmp_m4a) and os.path.getsize(tmp_m4a) > 0:
            shutil.move(tmp_m4a, out_path)
            return
        # Fallback: plain AIFF (higher quality but larger). We'll save as .aiff alongside .m4a path
        tmp_aiff = os.path.join(tmpdir, 'tmp.aiff')
        cmd2 = ['say', '-v', voice, '-o', tmp_aiff, text]
        subprocess.run(cmd2, check=True)
        if not (os.path.exists(tmp_aiff) and os.path.getsize(tmp_aiff) > 0):
            raise RuntimeError('say produced no audio')
        aiff_out = os.path.splitext(out_path)[0] + '.aiff'
        shutil.move(tmp_aiff, aiff_out)
    finally:
        try: shutil.rmtree(tmpdir)
        except OSError: pass

def build_text(obj):
    # Prefer paragraphs; fallback to title+body
    paras = obj.get('paragraphs')
    if not paras:
        body = obj.get('body') or ''
        paras = [body]
    title = obj.get('title')
    if title:
        return title + '. ' + ' '.join(paras)
    return ' '.join(paras)

def main():
    if not os.path.isdir(FACTS_DIR):
        print('facts dir not found:', FACTS_DIR)
        return
    ensure_dir(OUT_DIR)
    total, made = 0, 0
    for theme in os.listdir(FACTS_DIR):
        tdir = os.path.join(FACTS_DIR, theme)
        if not os.path.isdir(tdir):
            continue
        out_theme = os.path.join(OUT_DIR, theme)
        ensure_dir(out_theme)
        for name in os.listdir(tdir):
            if not name.endswith('.json'): continue
            base, lang = name.rsplit('.',1)[0].rsplit('_',1)
            in_path = os.path.join(tdir, name)
            out_path = os.path.join(out_theme, f"{base.split('/')[-1]}_{lang}.m4a")
            total += 1
            # Skip if non-empty already exists
            if os.path.exists(out_path) and os.path.getsize(out_path) > 0:
                continue
            with open(in_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            text = build_text(data)
            voice = VOICE_EN if lang == 'en' else VOICE_TH
            # Validate/select an installed voice
            voice = choose_voice(voice, 'en_' if lang=='en' else 'th_')
            try:
                say_to_m4a(text, voice, out_path)
                made += 1
                print('ok', out_path)
            except Exception as e:
                print('ERR', e, 'for', in_path)
                # Remove any zero-byte leftovers
                try:
                    if os.path.exists(out_path) and os.path.getsize(out_path) == 0:
                        os.remove(out_path)
                except OSError:
                    pass
    print(f"Done. {made} new files (of {total} facts). Output: {OUT_DIR}")

if __name__ == '__main__':
    main()
