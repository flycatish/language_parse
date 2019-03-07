#!/usr/bin/python
# -*- coding: utf-8 -*-
from lib import feeling

sentence = """AWSの有名なサービスにAmazon Elastic Compute Cloud (EC2) とAmazon Simple Storage Service (S3) がある。
これまでのクライアントが保有していた物理的なサーバファームと比較してAWSは大規模な計算処理能力を速やかに提供出来ることが強みである。こんとん"""

while(True):
    a = input("sentence:")
    result = feeling.first_deal(a)
    print(result)

