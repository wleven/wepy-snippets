#-*- coding: utf-8 -*-
import os
import simplejson as json
import codecs

def load_raw_snippets(src):
    with codecs.open(src, encoding='utf-8') as fin:
        return json.load(fin, encoding='utf-8', parse_float=False)

def include_snippets_body(snippet):
    body = snippet['body']
    if not isinstance(body, (str,unicode)):
        return
    if not body.startswith("@includes/"):
        return
    print("processing %s \n" % body)
    filepath = body[1:]
    if not os.path.exists(filepath):
        print("Failed to find includes file: %s" % body)
        return

    lines = codecs.open(filepath, encoding='utf-8').readlines()
    snippet['body'] = lines

def ensure_snippet_prefix(snippet, key):
    if not snippet.get('prefix'):
        snippet['prefix'] = key
    
    

def make_snippets(src):
    work_dir = os.path.abspath(__file__)
    if not os.path.exists(src):
        print("Failed to find file: %s/%s", work_dir,src)
        return
    snippets_dict = load_raw_snippets(src)
    for (key,snippet) in snippets_dict.iteritems():
       ensure_snippet_prefix(snippet, key)
       include_snippets_body(snippet)
    
    snippets_dest = os.path.join('../snippets',src)
    with codecs.open(snippets_dest, mode='w', encoding='utf-8') as fout:
        json.dump(snippets_dict, fout, ensure_ascii=False, encoding='utf-8',indent=2, sort_keys=True)

    print("Make snippets %s done!\n" % src)

def main():
    make_snippets('vue.json')    
    make_snippets('api.json')    

if __name__ == '__main__':
    main()