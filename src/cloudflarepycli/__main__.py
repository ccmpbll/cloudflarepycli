# -*- coding: utf-8 -*-
"""

Uses cloudflareclass.py to generate statistics for current ISP which approximate those generated by Cloudflares's
browser interface.

no arguments required:
    
    --debug write trace of io using logger (default does not)
    --json  out put to sysout is json rather than formatted printing

Created on Mon Nov  8 13:39:48 2021

@author: tevsl
"""
def main():
    try:
        from . import cloudflareclass
    except:
        import cloudflareclass
    import json
    import argparse
    
    thetester=cloudflareclass.cloudflare() #open first with no args to get version
    version=thetester.version
    thetester=None
    
    parser=argparse.ArgumentParser(description='Runs speed test of net connection using ping and Cloudflare')
    parser.add_argument('--debug',action='store_true',help='log network io')
    parser.add_argument('--json',action='store_true',help='write json to sysout instead of formatted results')
    parser.add_argument('--version',action='version',version='%(prog)s version '+str(version))
    args=parser.parse_args()
    
    thetester=cloudflareclass.cloudflare(debug=args.debug,printit=(not args.json)) #reopen with correct params
    thedict=thetester.runalltests()
    if args.json:
        print (json.dumps(thedict))
        
    #test deprecated rountines
    print (thetester.getcolo())
    print (thetester.getcolodetails(""))
    print (thetester.getisp(""))

if __name__=='__main__':
    main()
    
