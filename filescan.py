import argparse


parser=argparse.ArgumentParser(description="Subdomain enumeration", formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-d", "--domain", help="domain name for subdomain enumeration", type=str, required=True)
parser.add_argument("-o","--output", help="output filename to save the results", type=str, required=True)
parser.add_argument("-a", "--api", help="Security trails api key", type=str, required=True)
args=parser.parse_args()

