from common.RestClient import HttpClient
from common.read_file import read_yaml


class PayoutApi:
    def __init__(self):
        self.token = read_yaml("./common/extract.yaml")["token"]

    def payout_list(self,page_num,page_size):
        """
        支付列表
        :return:
        {
  "code": 200,
  "message": "Success",
  "data": {
    "total_item": 68,
    "total_page": 7,
    "item_list": [
      {
        "reference_id": "P240108-WAJUPAIS",
        "payout_id": "50f00994-627a-4721-8f33-0740438d20f3",
        "beneficiary_name": "Invent Enterprises",
        "payment_date": "2024-01-09T00:00:00+08:00",
        "complete_time": "2024-01-24T18:00:24+08:00",
        "create_time": "2024-01-08T14:16:40+08:00",
        "review_status": "passed",
        "payout_status": "completed",
        "amount": "10",
        "currency": "USD"
      },
      {
        "reference_id": "P240108-NAKVFFJA",
        "payout_id": "84576733-e0e8-4c28-9ef8-ad96e0f268f9",
        "beneficiary_name": "Invent Enterprises",
        "payment_date": "2024-01-08T00:00:00+08:00",
        "complete_time": null,
        "create_time": "2024-01-08T14:16:38+08:00",
        "review_status": "rejected",
        "payout_status": "pending",
        "amount": "10",
        "currency": "USD"
      },
      {
        "reference_id": "P240108-HOELIWSW",
        "payout_id": "840de61e-ff38-4fee-bffd-934ab3e7f6c1",
        "beneficiary_name": "Invent Enterprises",
        "payment_date": "2024-01-08T00:00:00+08:00",
        "complete_time": null,
        "create_time": "2024-01-08T14:16:37+08:00",
        "review_status": "rejected",
        "payout_status": "pending",
        "amount": "10",
        "currency": "USD"
      },
      {
        "reference_id": "P240108-SQCNSRSM",
        "payout_id": "5c848ec7-5c16-4d32-af4a-a7bc00b4d3d4",
        "beneficiary_name": "Invent Enterprises",
        "payment_date": "2024-01-08T00:00:00+08:00",
        "complete_time": null,
        "create_time": "2024-01-08T14:16:37+08:00",
        "review_status": "rejected",
        "payout_status": "pending",
        "amount": "10",
        "currency": "USD"
      },
      {
        "reference_id": "P240108-4M2LSXSA",
        "payout_id": "3a6da1f3-0951-4a0d-83ef-0159f692e75c",
        "beneficiary_name": "Invent Enterprises",
        "payment_date": "2024-01-08T00:00:00+08:00",
        "complete_time": null,
        "create_time": "2024-01-08T14:16:32+08:00",
        "review_status": "reviewing",
        "payout_status": "pending",
        "amount": "10",
        "currency": "USD"
      },
      {
        "reference_id": "P240108-IDR8I7DV",
        "payout_id": "9e2f9f7a-ef38-4ea9-bc44-9740cfd883b9",
        "beneficiary_name": "Invent Enterprises",
        "payment_date": "2024-01-08T00:00:00+08:00",
        "complete_time": "2024-01-08T16:33:20+08:00",
        "create_time": "2024-01-08T14:14:13+08:00",
        "review_status": "passed",
        "payout_status": "completed",
        "amount": "10",
        "currency": "USD"
      },
      {
        "reference_id": "P240108-8U1VMHOL",
        "payout_id": "113392e9-9da6-40e6-a2af-229ecfe31877",
        "beneficiary_name": "Invent Enterprises",
        "payment_date": "2024-01-09T00:00:00+08:00",
        "complete_time": null,
        "create_time": "2024-01-08T14:11:25+08:00",
        "review_status": "reviewing",
        "payout_status": "pending",
        "amount": "10",
        "currency": "USD"
      },
      {
        "reference_id": "P240108-K4TEWUAK",
        "payout_id": "93943b02-8fbd-455a-9a4a-f1d069fb1352",
        "beneficiary_name": "Invent Enterprises",
        "payment_date": "2024-01-08T00:00:00+08:00",
        "complete_time": null,
        "create_time": "2024-01-08T14:11:23+08:00",
        "review_status": "reviewing",
        "payout_status": "pending",
        "amount": "10",
        "currency": "USD"
      },
      {
        "reference_id": "P240108-Z8YX2HCB",
        "payout_id": "ae74caeb-7bd1-4994-be8c-ae5928847345",
        "beneficiary_name": "Invent Enterprises",
        "payment_date": "2024-01-08T00:00:00+08:00",
        "complete_time": null,
        "create_time": "2024-01-08T14:11:18+08:00",
        "review_status": "reviewing",
        "payout_status": "pending",
        "amount": "10",
        "currency": "USD"
      },
      {
        "reference_id": "P240108-HBDZKTBA",
        "payout_id": "f7b8797b-5400-433b-a5bd-49765e039652",
        "beneficiary_name": "Invent Enterprises",
        "payment_date": "2024-01-08T00:00:00+08:00",
        "complete_time": "2024-01-08T16:31:50+08:00",
        "create_time": "2024-01-08T13:56:46+08:00",
        "review_status": "passed",
        "payout_status": "completed",
        "amount": "10",
        "currency": "USD"
      }
    ]
  }
}
        """
        url = f"/api/v1/payout/list?page_num={page_num}&page_size={page_size}&date_type=create_time"
        headers = {
            "x-auth-token": self.token
        }
        return HttpClient().send_request(method="get", url=url, headers=headers)
