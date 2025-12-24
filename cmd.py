import subprocess


def run_cmd(cmd, check=True):
    """执行命令并返回(是否成功, 输出)"""
    try:
        result = subprocess.run(
            cmd,
            check=check,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8'
        )
        if result.returncode != 0:
            return False, result.stderr.strip()
        return True, result.stdout.strip()
    except FileNotFoundError as e:
        return False, f"命令未找到: {e.filename}"
    except subprocess.CalledProcessError as e:
        return False, f"执行失败:\nstdout: {e.stdout}\nstderr: {e.stderr}"
    except Exception as e:
        return False, f"未知错误: {e}"


def check_java():
    """检查 Java 是否已安装"""
    success, _ = run_cmd(["java", "-version"], check=False)
    # 'java -version' 成功时通常返回 0，但某些发行版会返回 1 并将输出写入 stderr
    # 我们只关心命令是否能被找到并执行
    return success

