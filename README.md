# SERVERLESS1

## 環境

```shell
> node -v
v16.13.1
> npm -v
8.1.2
> serverless -v
Framework Core: 3.12.0
Plugin: 6.2.1
SDK: 4.3.2
```

## local環境の設定

```shell
npm i -g serverless-offline serverless-dynamodb-local
sls dynamodb install
sls offline
sls start
```

### aws cliでdynamodbのテーブルを確認

```shell
> aws dynamodb list-tables --endpoint-url http://localhost:8000
{
    "TableNames": [
        "Chat"
    ]
}
```