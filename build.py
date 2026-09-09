# Copyright (c) 2026 Sayad Md Bayezid Hosan (Smartgen Platform)
import os
from smartgen_docs.core import Builder

def main():
    config_file = "smartgen.yml"
    output_dir = "site"
    
    print(f"Building documentation with Book theme...")
    if not os.path.exists(config_file):
        raise FileNotFoundError(f"Configuration file {config_file} not found!")
        
    # Shudhumatro core builder config path diye initialize kora hocche
    builder = Builder(
        config_path=config_file, 
        site_dir=output_dir
    )
    
    builder.build()
    print(f"Build successfully completed with Book theme in '{output_dir}/'!")

if __name__ == "__main__":
    main()