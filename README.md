# grow-the-glass

その日にコミットがなければLINEに通知を送ります。

## 依存関係

- requests
- BeautifulSoup4

## 使い方
以下を書いた `config.json` を同じフォルダに置く。

```json
{
  "username": "<your github username>",
  "line_token": "<your line token>"
}
```

あとは `cron` などで以下を実行。

```bash
$ python grow-the-glass.py
```
