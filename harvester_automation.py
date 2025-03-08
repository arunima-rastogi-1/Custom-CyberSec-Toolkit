##A Python script to automate theHarvester reconnaissance made by Arunima Rastogi
import os

def run_theharvester(target_domain):
    """
    Automates theHarvester to gather reconnaissance data for a target domain.
    Saves results as an HTML report.
    """
    output_file = f"{target_domain}_report.html"
    command = f"theHarvester -d {target_domain} -b all -f {output_file}"
    
    print(f"Running: {command}")
    os.system(command)
    print(f"Recon report saved as {output_file}")

if __name__ == "__main__":
    target_domain = input("Enter target domain: ")
    run_theharvester(target_domain)
