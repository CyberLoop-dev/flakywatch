#!/usr/bin/env python3
"""Identify tests with mixed pass/fail outcomes across JUnit XML reports."""
import argparse,json,sys,xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path
def read_report(path,results):
 root=ET.parse(path).getroot()
 for case in root.iter("testcase"):
  key=(case.attrib.get("classname",""),case.attrib.get("name",""))
  failed=any(child.tag in ("failure","error") for child in case); skipped=any(child.tag=="skipped" for child in case)
  results[key].append("skipped" if skipped else "failed" if failed else "passed")
def main():
 ap=argparse.ArgumentParser(description=__doc__); ap.add_argument("reports",nargs="+",type=Path); ap.add_argument("--json",action="store_true"); args=ap.parse_args()
 files=[]
 for item in args.reports: files.extend(sorted(item.glob("*.xml")) if item.is_dir() else [item])
 results=defaultdict(list)
 try:
  for path in files: read_report(path,results)
 except (OSError,ET.ParseError) as exc: print("Cannot read report: "+str(exc),file=sys.stderr); return 2
 flaky=[]
 for (klass,name),states in sorted(results.items()):
  if "passed" in states and "failed" in states: flaky.append({"class":klass,"name":name,"passed":states.count("passed"),"failed":states.count("failed"),"skipped":states.count("skipped")})
 report={"reports":len(files),"tests":len(results),"flaky":flaky}
 if args.json: print(json.dumps(report,indent=2))
 else:
  for item in flaky: print(f"FLAKY {item['class']}::{item['name']} ({item['passed']} pass / {item['failed']} fail)")
  print(f"{len(flaky)} flaky test(s) across {len(files)} report(s)")
 return 1 if flaky else 0
if __name__=="__main__": sys.exit(main())
