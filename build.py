# Copyright (c) 2026 Sayad Md Bayezid Hosan (Smartgen Platform)
import os
from smartgen_docs.core import Builder

def main():
    config_file = "smartgen.yml"
    output_dir = "site"
    
    print(f"Building documentation using {config_file}...")
    if not os.path.exists(config_file):
        raise FileNotFoundError(f"Configuration file {config_file} not found!")
        
    builder = Builder(config_path=config_file, site_dir=output_dir)
    builder.build()
    print(f"Build complete! Output generated in '{output_dir}/' directory.")

if __name__ == "__main__":
    main()