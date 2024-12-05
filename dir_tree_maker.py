import os

# ユニコードを使った特殊文字の定義
BRANCH = '\u251C\u2500\u2500 '  # ├──
LAST_BRANCH = '\u2514\u2500\u2500 '  # └──
VERTICAL = '\u2502   '  # │
SPACE = '    '  # 空白

def print_tree(directory, prefix="", add_space=False):
    """
    ディレクトリのツリー構造を出力します。
    
    :param directory: ディレクトリのパス
    :param prefix: 出力時の接頭辞（階層構造を表現するため）
    :param add_space: フォルダー間に空行を追加するかどうか
    """
    try:
        # ディレクトリ内のエントリをソートして取得
        entries = sorted(os.listdir(directory))
    except PermissionError:
        # アクセス権がない場合
        print(prefix + LAST_BRANCH + "[権限がありません]")
        return

    for i, entry in enumerate(entries):
        path = os.path.join(directory, entry)
        is_last = (i == len(entries) - 1)  # 最後のエントリかどうかを判定
        connector = LAST_BRANCH if is_last else BRANCH

        # エントリを出力
        print(prefix + connector + entry)

        # ディレクトリの場合、再帰的に探索
        if os.path.isdir(path):
            new_prefix = prefix + (SPACE if is_last else VERTICAL)
            print_tree(path, new_prefix, add_space=True)

        # フォルダー間に空行を追加
        if add_space and is_last:
            print(prefix + SPACE)

def main():
    # ユーザーからディレクトリのパスを入力
    directory = input("ツリー構造を出力するディレクトリのパスを入力してください: ").strip()

    # 入力されたパスの検証
    if not os.path.isdir(directory):
        print(f"エラー: {directory} は有効なディレクトリではありません。")
        return

    print(f"\nディレクトリツリー: {directory}\n")
    print_tree(directory)

if __name__ == "__main__":
    main()
