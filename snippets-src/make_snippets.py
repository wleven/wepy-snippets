#-*- coding: utf-8 -*-
import sys
import os
import simplejson as json
import codecs

class LogColor(object):
    RED   = "\033[1;31m"
    BLUE  = "\033[1;34m"
    CYAN  = "\033[1;36m"
    GREEN = "\033[0;32m"
    RESET = "\033[0;0m"
    BOLD    = "\033[;1m"
    REVERSE = "\033[;7m"

def log_error(msg):
    sys.stdout.write(LogColor.RED)
    print(msg)
    sys.stdout.write(LogColor.RESET)

def log_success(msg):
    sys.stdout.write(LogColor.GREEN)
    print(msg)
    sys.stdout.write(LogColor.RESET)


def load_raw_snippets(src):
    with codecs.open(src, encoding='utf-8') as fin:
        return json.load(fin, encoding='utf-8', parse_float=False)

def include_snippets_body(snippet, key, includes_dir):
    # if we did not specify the body field
    # then using the key as the filenameWithoutSuffix
    # then find a matching file in `includes` dir.
    body = snippet.get('body')
    filepath = None
    if body:
        if not isinstance(body, (str,unicode)):
            return
        if not body.startswith("@includes/"):
            return
        print("processing %s \n" % body)
        filepath = body[1:]
        if not os.path.exists(filepath):
            log_error("Failed to find includes file body= %s, key=%s, filepath=%s" % (body,key, filepath))
            return
    else:
        # find first matching file
        for filename in os.listdir(includes_dir):
            filenameWithoutSuffix = filename.rsplit('.', 1)[0]
            fpath =  os.path.join(includes_dir, filename)
            if filenameWithoutSuffix == key and os.path.isfile(fpath):
                filepath = fpath
                break
        if not filepath:
            log_error("Failed to find includes default file key=%s" % key )
            return

    lines = [] 
    for line in  codecs.open(filepath, encoding='utf-8').readlines():
        lineWithNewline = line.rstrip()
        lines.append(lineWithNewline)
    snippet['body'] = lines

def ensure_snippet_prefix(snippet, key):
    if not snippet.get('prefix'):
        snippet['prefix'] = key

def merge_snippet_options(snippet, options):
    # value in snippet should have high priority
    result_dict = dict(options)
    result_dict.update(snippet)
    snippet.update(result_dict)

def make_snippets(src, includes_dir="includes", global_options=None):
    work_dir = os.path.abspath(__file__)
    if not os.path.exists(src):
        log_error("Failed to find file: %s/%s" % (work_dir,src))
        return
    snippets_dict = load_raw_snippets(src)
    for (key,snippet) in snippets_dict.iteritems():
       ensure_snippet_prefix(snippet, key)
       include_snippets_body(snippet, key, includes_dir)
       if global_options:
           merge_snippet_options(snippet, global_options)

    snippets_dest = os.path.join('../snippets',src)
    with codecs.open(snippets_dest, mode='w', encoding='utf-8') as fout:
        json.dump(snippets_dict, fout, ensure_ascii=False, encoding='utf-8',indent=2, sort_keys=True)

    log_success("Make snippets %s done!\n" % src)

def main():
    make_snippets('wepy_html.json', includes_dir="includes/wepy_html", global_options={
        "scope": "vue,html,vue-html,wpy"
    })
    make_snippets('weui.json', includes_dir="includes/weui", global_options={
        "scope": "vue,html,vue-html,wpy"
    })
    make_snippets('wepy_api.json', includes_dir="includes/wepy_api", global_options={
        "scope": "javascript,typescript"
    })

if __name__ == '__main__':
    main()
