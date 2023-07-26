---
title: About Mathesar
description: 
published: true
date: 2023-07-19T23:28:52.216Z
tags: 
editor: markdown
dateCreated: 2022-01-21T01:34:45.667Z
---

# Mathesarとは

> Mathesarは現在開発中であり、2022年半ばにアーリーアダプター向けの準備が整う予定です。
{.is-warning}

Mathesarは、データベースへの直感的なユーザインタフェースを提供するオープンソースツールです。私たちの目的は、技術者でないユーザが、データベースの概念に関する予備知識なしに、データベースを簡単に扱えるようにすることです。私たちは、[Dabble DB](https://wiki.mathesar.org/en/product/concepts) のユーザーエクスペリエンスに大きく触発されています。

ユーザーは、ゼロからデータベースをセットアップするか、既存のデータベースに接続することができます。ユーザーは、データを保存し、整理し、さまざまなビューを設定することができます。ベータ版では、他のユーザーとのコラボレーション、データのビジュアライゼーション、ニーズの変化に応じたデータモデルの進化も可能になります。

Mathesarは、ユーザー自身のサーバーでセルフホスティングできるように設計されています。  

## ユースケース
***
Mathesarは以下のような用途に使用できます：
* 公共データセットの公開や探索
* 次のようなビジネスプロセスの実行：
  * 在庫管理
  * イベント企画
  * プロジェクト・タスク管理
  * 支出追跡と会計
  * 顧客関係管理
* 技術者でないユーザーに既存のデータベースへのアクセスを提供：
  * データ入力
  * カスタムレポートとクエリ
* 一般の人々や外部の協力者からデータの収集と処理（Googleフォームのような製品と似ています）
* 簡単なデータクリーニング（例：異なるソースから収集したデータを1つのフォーマットに統合すること）
* 簡単なデータ解析とビジュアライゼーション
* 接続されたデータベースと対話するためのREST APIの自動生成

Mathesarの目標は、情報を扱うすべての人々のためのインフラストラクチャー・ツールになることであり、私たちは、人々が考え出す他のユースケースを楽しみにしています。

## なぜMathesarを開発するのか？
***
データベース管理のGUI、表計算ソフト、「ローコード」プラットフォーム、ビジネスインテリジェンスツールなど、データを扱うためのツールはすでにたくさんあります。ではなぜ他のツールが必要なのでしょうか？
### 相互運用性とデータのポータビリティ
ほとんどの同等のツールを使って保存されたデータであっても、他のソフトウェアで変更することはできません。Mathesarは、相互運用可能なツールの活発なエコシステムとともに汎用データベース(Postgres)を使用しています。
### 親しみやすいユーザーエクスペリエンス
既存のツールでは、利用できる機能が制限されていたり、パワーユーザー向けになっていたりします。Mathesarは、ユーザーの技術レベルに合わせると同時に、高度な機能をサポートし、学習を促します。
### データの完全性と再利用
スプレッドシートやローコードプラットフォームは、デフォルトではデータの一貫性を確保するための機能があまりなく、再利用の可能性が制限されます。データベースは、設計上、この点では優れています。
### オープンソースインフラストラクチャ
データは貴重なものであり、特定の専用サービスを使うことに縛られるべきではありません。人々が自分自身のデータを管理するために、オープンソースで、分散化された、プライベートなインフラが必要なのです。


## さらに詳しい内容は
- [ツールカテゴリの探索 *Mathesarの適用範囲を定義するための初期調査報告書*](/en/design/reports/tool-category) 
- [製品コンセプト *Mathesarのコンセプト*](/en/product/concepts) 
{.links-list}

## Credits
Thanks to Shinji Matsumoto for translating this page from English to Japanese.