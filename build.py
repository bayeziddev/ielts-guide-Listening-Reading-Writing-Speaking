# Copyright (c) 2026 Sayad Md Bayezid Hosan (Smartgen Platform)
import os
import shutil
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
    # SmartGen builds Markdown pages but does not copy custom documentation assets.
    # Keep learner-facing diagrams available at the same relative URLs used in Markdown.
    image_source = os.path.join("docs", "images")
    image_target = os.path.join(output_dir, "images")
    if os.path.isdir(image_source):
        shutil.copytree(image_source, image_target, dirs_exist_ok=True)
    print(f"Build successfully completed with Book theme in '{output_dir}/'!")

if __name__ == "__main__":
    main()
