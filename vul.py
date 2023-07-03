#!/usr/bin/env python
import scanner
target_url = "http://192.168.221.6"
vuln_scanner = scanner.Scanner(target_url)
vuln_scanner.crawl(target_url)
print(target_url)