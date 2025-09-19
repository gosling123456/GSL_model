import os
import shutil
import argparse

def replicate_directory_structure(source_dir, target_dir):
    """
    复制源目录的结构到目标目录，但不复制任何文件
    
    参数:
        source_dir (str): 源目录路径
        target_dir (str): 目标目录路径
    """
    # 确保目标目录存在
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    # 遍历源目录的所有子目录
    for root, dirs, files in os.walk(source_dir):
        # 计算相对于源目录的路径
        relative_path = os.path.relpath(root, source_dir)
        
        # 如果相对路径是当前目录，则跳过（已经是目标目录）
        if relative_path == '.':
            continue
            
        # 构建目标路径
        target_path = os.path.join(target_dir, relative_path)
        
        # 如果目标路径不存在，则创建
        if not os.path.exists(target_path):
            os.makedirs(target_path)
            print(f"创建目录: {target_path}")

def main():
    # 设置命令行参数解析
    parser = argparse.ArgumentParser(description='复制目录结构而不复制文件内容')
    parser.add_argument('source', help='源目录路径')
    parser.add_argument('target', help='目标目录路径')
    
    args = parser.parse_args()
    
    # 检查源目录是否存在
    if not os.path.exists(args.source):
        print(f"错误: 源目录 '{args.source}' 不存在")
        return
    
    # 执行目录结构复制
    replicate_directory_structure(args.source, args.target)
    print(f"完成! 已从 '{args.source}' 复制目录结构到 '{args.target}'")

if __name__ == "__main__":
    main()