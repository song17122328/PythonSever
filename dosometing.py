# -*- coding: UTF-8 -*-
"""
@Introduce：
@Project ：NestedTree_ExcelToJSON.py 
@File ：dosometing.py
@Author ：小小小松
@Date ：2023/5/25 17:51
"""
import json
import csv

json_data = '''
[
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "electronegativity of na",
        "ParentId": "b1075b1e-4cf3-416e-ad3c-c13160479601",
        "Score": 0,
        "TreeType": "feature",
        "_id": "ade538bb-70dc-4faa-8ddb-f472bc5e9d77"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "electronegativity of dopant d2",
        "ParentId": "b1075b1e-4cf3-416e-ad3c-c13160479601",
        "Score": 0,
        "TreeType": "feature",
        "_id": "5a9bdcff-cdc0-43f5-bcc1-1af196e3a1e8"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "electronegativity of dopant d3",
        "ParentId": "b1075b1e-4cf3-416e-ad3c-c13160479601",
        "Score": 0,
        "TreeType": "feature",
        "_id": "7b9cdb66-3f3c-4f20-b451-5b760e546617"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "calculated effective electronegativity according to formula (na)",
        "ParentId": "b1075b1e-4cf3-416e-ad3c-c13160479601",
        "Score": 0,
        "TreeType": "feature",
        "_id": "5b3ecc17-0798-4ed5-9f4b-0f6e4467c280"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "calculated effective electronegativity according to formula (d2)",
        "ParentId": "b1075b1e-4cf3-416e-ad3c-c13160479601",
        "Score": 0,
        "TreeType": "feature",
        "_id": "835bb3d9-3c9b-4b62-90d5-da239a0cb33b"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "calculated effective electronegativity according to formula (d3)",
        "ParentId": "b1075b1e-4cf3-416e-ad3c-c13160479601",
        "Score": 0,
        "TreeType": "feature",
        "_id": "011d20ee-2485-409b-b486-cbacea052673"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "electronegativity of element m1",
        "ParentId": "b1075b1e-4cf3-416e-ad3c-c13160479601",
        "Score": 0,
        "TreeType": "feature",
        "_id": "a6ab187b-e93d-459a-acca-c275649656b2"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "electronegativity of element m2",
        "ParentId": "b1075b1e-4cf3-416e-ad3c-c13160479601",
        "Score": 0,
        "TreeType": "feature",
        "_id": "f5535a26-35ae-4f54-b6e6-ed72c68dbc46"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "electronegativity of element x1",
        "ParentId": "b1075b1e-4cf3-416e-ad3c-c13160479601",
        "Score": 0,
        "TreeType": "feature",
        "_id": "4bee360f-0db9-4116-ac4d-1a9e13c90f7b"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "electronegativity of element x2",
        "ParentId": "b1075b1e-4cf3-416e-ad3c-c13160479601",
        "Score": 0,
        "TreeType": "feature",
        "_id": "2d5e0447-b09c-49b5-951c-c7bc025e99e2"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "average effective electronegativity of m site",
        "ParentId": "b1075b1e-4cf3-416e-ad3c-c13160479601",
        "Score": 0,
        "TreeType": "feature",
        "_id": "91e2b115-178c-4736-820b-54b3e7efb620"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "average effective electronegativity of x site",
        "ParentId": "b1075b1e-4cf3-416e-ad3c-c13160479601",
        "Score": 0,
        "TreeType": "feature",
        "_id": "5232ab72-799e-4eab-a6b0-b4a64d99db5d"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "average electronegativity of m site",
        "ParentId": "b1075b1e-4cf3-416e-ad3c-c13160479601",
        "Score": 0,
        "TreeType": "feature",
        "_id": "aca94e82-3ce9-4d06-834c-bb6aef754f1d"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "standard deviation of electronegativity in m site",
        "ParentId": "b1075b1e-4cf3-416e-ad3c-c13160479601",
        "Score": 0,
        "TreeType": "feature",
        "_id": "2a403c56-6df6-406e-886e-c64becd3527e"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "maximum deviation of electronegativity in m site",
        "ParentId": "b1075b1e-4cf3-416e-ad3c-c13160479601",
        "Score": 0,
        "TreeType": "feature",
        "_id": "e0a36dae-e409-4e9c-9468-7ab1d6c0e806"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "average electronegativity of a site",
        "ParentId": "b1075b1e-4cf3-416e-ad3c-c13160479601",
        "Score": 0,
        "TreeType": "feature",
        "_id": "3324ee26-235f-4a2d-862f-7746a3b5ccda"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "standard deviation of electronegativity in a site",
        "ParentId": "b1075b1e-4cf3-416e-ad3c-c13160479601",
        "Score": 0,
        "TreeType": "feature",
        "_id": "c47b65dd-5ec5-4c4d-914f-c94587a12c9c"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "maximum deviation of electronegativity in a site",
        "ParentId": "b1075b1e-4cf3-416e-ad3c-c13160479601",
        "Score": 0,
        "TreeType": "feature",
        "_id": "d6772879-176f-4b7c-bab0-cc71b930ac15"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "x_m_avg-x_na",
        "ParentId": "b1075b1e-4cf3-416e-ad3c-c13160479601",
        "Score": 0,
        "TreeType": "feature",
        "_id": "20da9f9d-269e-40d8-b872-67084552e62b"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "x_m_avg-x_a",
        "ParentId": "b1075b1e-4cf3-416e-ad3c-c13160479601",
        "Score": 0,
        "TreeType": "feature",
        "_id": "59395943-84f2-4abd-887f-464bdefcd76b"
    },
    {
        "ChildrenId": [
            "ade538bb-70dc-4faa-8ddb-f472bc5e9d77",
            "5a9bdcff-cdc0-43f5-bcc1-1af196e3a1e8",
            "7b9cdb66-3f3c-4f20-b451-5b760e546617",
            "5b3ecc17-0798-4ed5-9f4b-0f6e4467c280",
            "835bb3d9-3c9b-4b62-90d5-da239a0cb33b",
            "011d20ee-2485-409b-b486-cbacea052673",
            "a6ab187b-e93d-459a-acca-c275649656b2",
            "f5535a26-35ae-4f54-b6e6-ed72c68dbc46",
            "4bee360f-0db9-4116-ac4d-1a9e13c90f7b",
            "2d5e0447-b09c-49b5-951c-c7bc025e99e2",
            "91e2b115-178c-4736-820b-54b3e7efb620",
            "5232ab72-799e-4eab-a6b0-b4a64d99db5d",
            "aca94e82-3ce9-4d06-834c-bb6aef754f1d",
            "2a403c56-6df6-406e-886e-c64becd3527e",
            "e0a36dae-e409-4e9c-9468-7ab1d6c0e806",
            "3324ee26-235f-4a2d-862f-7746a3b5ccda",
            "c47b65dd-5ec5-4c4d-914f-c94587a12c9c",
            "d6772879-176f-4b7c-bab0-cc71b930ac15",
            "20da9f9d-269e-40d8-b872-67084552e62b",
            "59395943-84f2-4abd-887f-464bdefcd76b"
        ],
        "ChildrenName": [
            "electronegativity of na",
            "electronegativity of dopant d2",
            "electronegativity of dopant d3",
            "calculated effective electronegativity according to formula (na)",
            "calculated effective electronegativity according to formula (d2)",
            "calculated effective electronegativity according to formula (d3)",
            "electronegativity of element m1",
            "electronegativity of element m2",
            "electronegativity of element x1",
            "electronegativity of element x2",
            "average effective electronegativity of m site",
            "average effective electronegativity of x site",
            "average electronegativity of m site",
            "standard deviation of electronegativity in m site",
            "maximum deviation of electronegativity in m site",
            "average electronegativity of a site",
            "standard deviation of electronegativity in a site",
            "maximum deviation of electronegativity in a site",
            "x_m_avg-x_na",
            "x_m_avg-x_a"
        ],
        "NodeName": "electronegativity",
        "ParentId": "bbd360da-3d6a-4cd2-be24-1bf7c8659689",
        "Score": 0,
        "TreeType": "feature",
        "_id": "b1075b1e-4cf3-416e-ad3c-c13160479601"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "ionic radius of na",
        "ParentId": "a65e26a4-e485-4461-8707-9c9f2b9bf5ac",
        "Score": 0,
        "TreeType": "feature",
        "_id": "7b9879b5-2cb8-45e3-9631-4f1055764c6c"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "ionic radius of formulaic leftmost dopant",
        "ParentId": "a65e26a4-e485-4461-8707-9c9f2b9bf5ac",
        "Score": 0,
        "TreeType": "feature",
        "_id": "3b83533c-5853-4ca7-81b7-a15050a75254"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "ionic radius of formulaic rightmost dopant",
        "ParentId": "a65e26a4-e485-4461-8707-9c9f2b9bf5ac",
        "Score": 0,
        "TreeType": "feature",
        "_id": "820afc8c-b2be-46d7-9e0c-022fc031f12b"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "calculated effective ionic radius according to formula(na)",
        "ParentId": "a65e26a4-e485-4461-8707-9c9f2b9bf5ac",
        "Score": 0,
        "TreeType": "feature",
        "_id": "1d8cbcb0-299c-482d-a98c-ce2ca0517f92"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "calculated effective ionic radius according to formula(d2)",
        "ParentId": "a65e26a4-e485-4461-8707-9c9f2b9bf5ac",
        "Score": 0,
        "TreeType": "feature",
        "_id": "14e10539-c5a7-44f1-b16c-07eb22ec5722"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "calculated effective ionic radius according to formula(d3)",
        "ParentId": "a65e26a4-e485-4461-8707-9c9f2b9bf5ac",
        "Score": 0,
        "TreeType": "feature",
        "_id": "c837c371-5804-4918-880e-037899990f6b"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "ionic radius of element m1",
        "ParentId": "a65e26a4-e485-4461-8707-9c9f2b9bf5ac",
        "Score": 0,
        "TreeType": "feature",
        "_id": "b2a06322-0d2d-402d-aa5e-8563c2554306"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "ionic radius of element m2",
        "ParentId": "a65e26a4-e485-4461-8707-9c9f2b9bf5ac",
        "Score": 0,
        "TreeType": "feature",
        "_id": "872bfa14-3244-4b72-a2fb-50fbbadffa30"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "ionic radius of element x1",
        "ParentId": "a65e26a4-e485-4461-8707-9c9f2b9bf5ac",
        "Score": 0,
        "TreeType": "feature",
        "_id": "8732b6a4-a1df-489a-8ee1-8df4f18a29d3"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "ionic radius of element x2",
        "ParentId": "a65e26a4-e485-4461-8707-9c9f2b9bf5ac",
        "Score": 0,
        "TreeType": "feature",
        "_id": "f0380df6-8eca-497c-92fc-5b81c5a2981b"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "average effective ionic radius of m site",
        "ParentId": "a65e26a4-e485-4461-8707-9c9f2b9bf5ac",
        "Score": 0,
        "TreeType": "feature",
        "_id": "d0bd3d1b-2d01-4c5f-bc37-8422d91a29c3"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "average effective ionic radius of x site",
        "ParentId": "a65e26a4-e485-4461-8707-9c9f2b9bf5ac",
        "Score": 0,
        "TreeType": "feature",
        "_id": "0c447418-f530-412a-8cf6-eb6802a5cc59"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "average radius of m site",
        "ParentId": "a65e26a4-e485-4461-8707-9c9f2b9bf5ac",
        "Score": 0,
        "TreeType": "feature",
        "_id": "b94bf7e6-5443-4056-94db-b9113c5b5061"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "standard deviation of radius in m site",
        "ParentId": "a65e26a4-e485-4461-8707-9c9f2b9bf5ac",
        "Score": 0,
        "TreeType": "feature",
        "_id": "37031132-c7e8-40db-87fa-cdbed71e1230"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "maximum deviation of radius in m site",
        "ParentId": "a65e26a4-e485-4461-8707-9c9f2b9bf5ac",
        "Score": 0,
        "TreeType": "feature",
        "_id": "f4a2a563-7a2a-42ca-8e65-736cc22a388e"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "average radius of a site",
        "ParentId": "a65e26a4-e485-4461-8707-9c9f2b9bf5ac",
        "Score": 0,
        "TreeType": "feature",
        "_id": "5bf7ff0a-c84e-490c-b678-2c4b8e979a84"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "standard deviation of radius in a site",
        "ParentId": "a65e26a4-e485-4461-8707-9c9f2b9bf5ac",
        "Score": 0,
        "TreeType": "feature",
        "_id": "ad1eefd2-3920-457b-89a7-90cbb0627ad6"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "maximum deviation of radius in a site",
        "ParentId": "a65e26a4-e485-4461-8707-9c9f2b9bf5ac",
        "Score": 0,
        "TreeType": "feature",
        "_id": "84d047f9-107e-4f05-8fda-957d13a6432c"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "r_m_avg/r_na",
        "ParentId": "a65e26a4-e485-4461-8707-9c9f2b9bf5ac",
        "Score": 0,
        "TreeType": "feature",
        "_id": "92fba10f-5655-4c78-b059-aed4a58bd7a2"
    },
    {
        "ChildrenId": [
            "7b9879b5-2cb8-45e3-9631-4f1055764c6c",
            "3b83533c-5853-4ca7-81b7-a15050a75254",
            "820afc8c-b2be-46d7-9e0c-022fc031f12b",
            "1d8cbcb0-299c-482d-a98c-ce2ca0517f92",
            "14e10539-c5a7-44f1-b16c-07eb22ec5722",
            "c837c371-5804-4918-880e-037899990f6b",
            "b2a06322-0d2d-402d-aa5e-8563c2554306",
            "872bfa14-3244-4b72-a2fb-50fbbadffa30",
            "8732b6a4-a1df-489a-8ee1-8df4f18a29d3",
            "f0380df6-8eca-497c-92fc-5b81c5a2981b",
            "d0bd3d1b-2d01-4c5f-bc37-8422d91a29c3",
            "0c447418-f530-412a-8cf6-eb6802a5cc59",
            "b94bf7e6-5443-4056-94db-b9113c5b5061",
            "37031132-c7e8-40db-87fa-cdbed71e1230",
            "f4a2a563-7a2a-42ca-8e65-736cc22a388e",
            "5bf7ff0a-c84e-490c-b678-2c4b8e979a84",
            "ad1eefd2-3920-457b-89a7-90cbb0627ad6",
            "84d047f9-107e-4f05-8fda-957d13a6432c",
            "92fba10f-5655-4c78-b059-aed4a58bd7a2"
        ],
        "ChildrenName": [
            "ionic radius of na",
            "ionic radius of formulaic leftmost dopant",
            "ionic radius of formulaic rightmost dopant",
            "calculated effective ionic radius according to formula(na)",
            "calculated effective ionic radius according to formula(d2)",
            "calculated effective ionic radius according to formula(d3)",
            "ionic radius of element m1",
            "ionic radius of element m2",
            "ionic radius of element x1",
            "ionic radius of element x2",
            "average effective ionic radius of m site",
            "average effective ionic radius of x site",
            "average radius of m site",
            "standard deviation of radius in m site",
            "maximum deviation of radius in m site",
            "average radius of a site",
            "standard deviation of radius in a site",
            "maximum deviation of radius in a site",
            "r_m_avg/r_na"
        ],
        "NodeName": "radius",
        "ParentId": "bbd360da-3d6a-4cd2-be24-1bf7c8659689",
        "Score": 0,
        "TreeType": "feature",
        "_id": "a65e26a4-e485-4461-8707-9c9f2b9bf5ac"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "volume of na",
        "ParentId": "aa4d8a28-f8ff-4b18-abff-1c89c0935f63",
        "Score": 0,
        "TreeType": "feature",
        "_id": "7495d05d-7462-409a-80e4-e5da707c32d6"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "volume of d2",
        "ParentId": "aa4d8a28-f8ff-4b18-abff-1c89c0935f63",
        "Score": 0,
        "TreeType": "feature",
        "_id": "cbdba811-7950-44d8-be2e-0cba2c968acd"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "volume of d3",
        "ParentId": "aa4d8a28-f8ff-4b18-abff-1c89c0935f63",
        "Score": 0,
        "TreeType": "feature",
        "_id": "0ad011eb-40f3-4699-95b6-f4d9fcb3bc57"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "calculated effective volume of species d1 according to formula (na)",
        "ParentId": "aa4d8a28-f8ff-4b18-abff-1c89c0935f63",
        "Score": 0,
        "TreeType": "feature",
        "_id": "ccbaa769-48f6-4ec8-993b-512b605a8808"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "calculated effective volume of species d2 according to formula (d2)",
        "ParentId": "aa4d8a28-f8ff-4b18-abff-1c89c0935f63",
        "Score": 0,
        "TreeType": "feature",
        "_id": "dbd1d723-5a13-4f34-b712-92d53155fff2"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "calculated effective volume of species d3 according to formula (d3)",
        "ParentId": "aa4d8a28-f8ff-4b18-abff-1c89c0935f63",
        "Score": 0,
        "TreeType": "feature",
        "_id": "3e59d56a-688e-420a-b7c2-3b99c6fc1695"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "volume per anion",
        "ParentId": "aa4d8a28-f8ff-4b18-abff-1c89c0935f63",
        "Score": 0,
        "TreeType": "feature",
        "_id": "1b728604-74ac-46df-8bfb-05663076789b"
    },
    {
        "ChildrenId": [
            "7495d05d-7462-409a-80e4-e5da707c32d6",
            "cbdba811-7950-44d8-be2e-0cba2c968acd",
            "0ad011eb-40f3-4699-95b6-f4d9fcb3bc57",
            "ccbaa769-48f6-4ec8-993b-512b605a8808",
            "dbd1d723-5a13-4f34-b712-92d53155fff2",
            "3e59d56a-688e-420a-b7c2-3b99c6fc1695",
            "1b728604-74ac-46df-8bfb-05663076789b"
        ],
        "ChildrenName": [
            "volume of na",
            "volume of d2",
            "volume of d3",
            "calculated effective volume of species d1 according to formula (na)",
            "calculated effective volume of species d2 according to formula (d2)",
            "calculated effective volume of species d3 according to formula (d3)",
            "volume per anion"
        ],
        "NodeName": "volume",
        "ParentId": "bbd360da-3d6a-4cd2-be24-1bf7c8659689",
        "Score": 0,
        "TreeType": "feature",
        "_id": "aa4d8a28-f8ff-4b18-abff-1c89c0935f63"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "valence of element m1",
        "ParentId": "d6b6ac4e-6601-497a-a10f-7304d40cfe69",
        "Score": 0,
        "TreeType": "feature",
        "_id": "6cde43bd-0937-48fb-9cc1-71bfa90d4586"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "valence of element m2",
        "ParentId": "d6b6ac4e-6601-497a-a10f-7304d40cfe69",
        "Score": 0,
        "TreeType": "feature",
        "_id": "5bfb8f81-caa9-4b55-947f-509b47625b27"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "valence of element x1",
        "ParentId": "d6b6ac4e-6601-497a-a10f-7304d40cfe69",
        "Score": 0,
        "TreeType": "feature",
        "_id": "a11d5c39-0dab-4f69-b2cb-c17d6adc7c94"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "valence of element x2",
        "ParentId": "d6b6ac4e-6601-497a-a10f-7304d40cfe69",
        "Score": 0,
        "TreeType": "feature",
        "_id": "ee3f857e-204b-4264-adcd-699b7635ef11"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "average effective ionic valence of m site",
        "ParentId": "d6b6ac4e-6601-497a-a10f-7304d40cfe69",
        "Score": 0,
        "TreeType": "feature",
        "_id": "2b17f4b0-846b-4064-8341-a61e9fd860df"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "average effective ionic valence of x site",
        "ParentId": "d6b6ac4e-6601-497a-a10f-7304d40cfe69",
        "Score": 0,
        "TreeType": "feature",
        "_id": "2fa55c2e-f348-41f4-ad8e-f2b0ffdef58d"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "average ionic charge states of m site",
        "ParentId": "d6b6ac4e-6601-497a-a10f-7304d40cfe69",
        "Score": 0,
        "TreeType": "feature",
        "_id": "c21885b1-fd96-4fd3-bc1c-99ae7f40f1ba"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "standard deviation of  ionic charge states in m site",
        "ParentId": "d6b6ac4e-6601-497a-a10f-7304d40cfe69",
        "Score": 0,
        "TreeType": "feature",
        "_id": "304277d6-a88d-4c0d-9b00-67c779ec02ea"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "maximum deviation of  ionic charge states in m site",
        "ParentId": "d6b6ac4e-6601-497a-a10f-7304d40cfe69",
        "Score": 0,
        "TreeType": "feature",
        "_id": "a4c16eb6-c25f-462d-8610-eb7768d7c04c"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "average ionic charge states of a site",
        "ParentId": "d6b6ac4e-6601-497a-a10f-7304d40cfe69",
        "Score": 0,
        "TreeType": "feature",
        "_id": "668213a0-e670-4dfa-a53d-1b8ab42717ef"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "standard deviation of  ionic charge states in a site",
        "ParentId": "d6b6ac4e-6601-497a-a10f-7304d40cfe69",
        "Score": 0,
        "TreeType": "feature",
        "_id": "13683f2e-7807-43b9-80c1-b89e636d6d1d"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "maximum deviation of  ionic charge states in a site",
        "ParentId": "d6b6ac4e-6601-497a-a10f-7304d40cfe69",
        "Score": 0,
        "TreeType": "feature",
        "_id": "7be54ef9-2fc7-4d69-b2b1-db1a6d57a812"
    },
    {
        "ChildrenId": [
            "6cde43bd-0937-48fb-9cc1-71bfa90d4586",
            "5bfb8f81-caa9-4b55-947f-509b47625b27",
            "a11d5c39-0dab-4f69-b2cb-c17d6adc7c94",
            "ee3f857e-204b-4264-adcd-699b7635ef11",
            "2b17f4b0-846b-4064-8341-a61e9fd860df",
            "2fa55c2e-f348-41f4-ad8e-f2b0ffdef58d",
            "c21885b1-fd96-4fd3-bc1c-99ae7f40f1ba",
            "304277d6-a88d-4c0d-9b00-67c779ec02ea",
            "a4c16eb6-c25f-462d-8610-eb7768d7c04c",
            "668213a0-e670-4dfa-a53d-1b8ab42717ef",
            "13683f2e-7807-43b9-80c1-b89e636d6d1d",
            "7be54ef9-2fc7-4d69-b2b1-db1a6d57a812"
        ],
        "ChildrenName": [
            "valence of element m1",
            "valence of element m2",
            "valence of element x1",
            "valence of element x2",
            "average effective ionic valence of m site",
            "average effective ionic valence of x site",
            "average ionic charge states of m site",
            "standard deviation of  ionic charge states in m site",
            "maximum deviation of  ionic charge states in m site",
            "average ionic charge states of a site",
            "standard deviation of  ionic charge states in a site",
            "maximum deviation of  ionic charge states in a site"
        ],
        "NodeName": "valence",
        "ParentId": "bbd360da-3d6a-4cd2-be24-1bf7c8659689",
        "Score": 0,
        "TreeType": "feature",
        "_id": "d6b6ac4e-6601-497a-a10f-7304d40cfe69"
    },
    {
        "ChildrenId": [
            "b1075b1e-4cf3-416e-ad3c-c13160479601",
            "a65e26a4-e485-4461-8707-9c9f2b9bf5ac",
            "aa4d8a28-f8ff-4b18-abff-1c89c0935f63",
            "d6b6ac4e-6601-497a-a10f-7304d40cfe69"
        ],
        "ChildrenName": [
            "electronegativity",
            "radius",
            "volume",
            "valence"
        ],
        "NodeName": "intrinsic-atomic parameter",
        "ParentId": "cf329d0d-2077-4962-b955-9a189e50f1bc",
        "Score": 0,
        "TreeType": "feature",
        "_id": "bbd360da-3d6a-4cd2-be24-1bf7c8659689"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "stoichiometric number of species m according to formula",
        "ParentId": "c837ae61-22bb-4403-b8a9-b840666d76d3",
        "Score": 0,
        "TreeType": "feature",
        "_id": "b5ca76eb-136d-4dc1-ae8d-21d406870431"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "stoichiometric number of species po4 according to formula",
        "ParentId": "c837ae61-22bb-4403-b8a9-b840666d76d3",
        "Score": 0,
        "TreeType": "feature",
        "_id": "22cd7db6-ed18-4282-821f-40ce4df7ad54"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "stoichiometric number of species na according to formula",
        "ParentId": "c837ae61-22bb-4403-b8a9-b840666d76d3",
        "Score": 0,
        "TreeType": "feature",
        "_id": "c743acd2-ef9f-4225-8c26-1a32e0423dc3"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "na+ concentration",
        "ParentId": "c837ae61-22bb-4403-b8a9-b840666d76d3",
        "Score": 0,
        "TreeType": "feature",
        "_id": "bd16c91c-6e25-4f07-bed5-f048faf0531f"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "na content",
        "ParentId": "c837ae61-22bb-4403-b8a9-b840666d76d3",
        "Score": 0,
        "TreeType": "feature",
        "_id": "d713233b-c5eb-489b-90a1-59343565f671"
    },
    {
        "ChildrenId": [
            "b5ca76eb-136d-4dc1-ae8d-21d406870431",
            "22cd7db6-ed18-4282-821f-40ce4df7ad54",
            "c743acd2-ef9f-4225-8c26-1a32e0423dc3",
            "bd16c91c-6e25-4f07-bed5-f048faf0531f",
            "d713233b-c5eb-489b-90a1-59343565f671"
        ],
        "ChildrenName": [
            "stoichiometric number of species m according to formula",
            "stoichiometric number of species po4 according to formula",
            "stoichiometric number of species na according to formula",
            "na+ concentration",
            "na content"
        ],
        "NodeName": "concentration",
        "ParentId": "75fb3b22-ba16-4465-bfb0-3292c30c0426",
        "Score": 0,
        "TreeType": "feature",
        "_id": "c837ae61-22bb-4403-b8a9-b840666d76d3"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "stoichiometric occupancy of d2 dopant position",
        "ParentId": "3d24ba63-a8a2-4caf-a993-70b079086d5b",
        "Score": 0,
        "TreeType": "feature",
        "_id": "38578545-d56b-4890-85c6-fc546e0f3848"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "occupancy of na+ in wyckoff 6b site",
        "ParentId": "3d24ba63-a8a2-4caf-a993-70b079086d5b",
        "Score": 0,
        "TreeType": "feature",
        "_id": "e3a173ed-cbcf-4059-90ac-ca28cb5d495a"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "occupancy of na+ in wyckoff 18e site",
        "ParentId": "3d24ba63-a8a2-4caf-a993-70b079086d5b",
        "Score": 0,
        "TreeType": "feature",
        "_id": "8524717f-48d2-4ba7-bdd3-b7cbcbc49d39"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "occupancy of na+ in wyckoff 36f site",
        "ParentId": "3d24ba63-a8a2-4caf-a993-70b079086d5b",
        "Score": 0,
        "TreeType": "feature",
        "_id": "566451a5-90c2-41b8-a433-258befb404a5"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "occupancy of element m1",
        "ParentId": "3d24ba63-a8a2-4caf-a993-70b079086d5b",
        "Score": 0,
        "TreeType": "feature",
        "_id": "2a8a5dbf-cfce-457d-8a5f-99ad116c798b"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "occupancy of element m2",
        "ParentId": "3d24ba63-a8a2-4caf-a993-70b079086d5b",
        "Score": 0,
        "TreeType": "feature",
        "_id": "1f33e7fd-b61d-4a2a-87b1-0ed9dac563b3"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "occupancy of element x1",
        "ParentId": "3d24ba63-a8a2-4caf-a993-70b079086d5b",
        "Score": 0,
        "TreeType": "feature",
        "_id": "e4e768c6-18d7-413c-9fec-0d396198fba6"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "occupancy of element x2",
        "ParentId": "3d24ba63-a8a2-4caf-a993-70b079086d5b",
        "Score": 0,
        "TreeType": "feature",
        "_id": "79cbb21b-4a0e-4e1f-8019-3d9d121ef06d"
    },
    {
        "ChildrenId": [
            "38578545-d56b-4890-85c6-fc546e0f3848",
            "e3a173ed-cbcf-4059-90ac-ca28cb5d495a",
            "8524717f-48d2-4ba7-bdd3-b7cbcbc49d39",
            "566451a5-90c2-41b8-a433-258befb404a5",
            "2a8a5dbf-cfce-457d-8a5f-99ad116c798b",
            "1f33e7fd-b61d-4a2a-87b1-0ed9dac563b3",
            "e4e768c6-18d7-413c-9fec-0d396198fba6",
            "79cbb21b-4a0e-4e1f-8019-3d9d121ef06d"
        ],
        "ChildrenName": [
            "stoichiometric occupancy of d2 dopant position",
            "occupancy of na+ in wyckoff 6b site",
            "occupancy of na+ in wyckoff 18e site",
            "occupancy of na+ in wyckoff 36f site",
            "occupancy of element m1",
            "occupancy of element m2",
            "occupancy of element x1",
            "occupancy of element x2"
        ],
        "NodeName": "occupancy",
        "ParentId": "75fb3b22-ba16-4465-bfb0-3292c30c0426",
        "Score": 0,
        "TreeType": "feature",
        "_id": "3d24ba63-a8a2-4caf-a993-70b079086d5b"
    },
    {
        "ChildrenId": [
            "c837ae61-22bb-4403-b8a9-b840666d76d3",
            "3d24ba63-a8a2-4caf-a993-70b079086d5b"
        ],
        "ChildrenName": [
            "concentration",
            "occupancy"
        ],
        "NodeName": "extrinsic-atomic parameter",
        "ParentId": "cf329d0d-2077-4962-b955-9a189e50f1bc",
        "Score": 0,
        "TreeType": "feature",
        "_id": "75fb3b22-ba16-4465-bfb0-3292c30c0426"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "standard deviation in li bond ionicity",
        "ParentId": "77f97fb4-ee17-4a81-8de7-8c09d4a7b772",
        "Score": 0,
        "TreeType": "feature",
        "_id": "1da84258-c62f-4bad-8a3c-9a975ed1c20c"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "average li bond ionicity",
        "ParentId": "77f97fb4-ee17-4a81-8de7-8c09d4a7b772",
        "Score": 0,
        "TreeType": "feature",
        "_id": "137d0b0e-8645-482d-be82-f450fe6307ea"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "average bond ionicity of sublattice",
        "ParentId": "77f97fb4-ee17-4a81-8de7-8c09d4a7b772",
        "Score": 0,
        "TreeType": "feature",
        "_id": "5d3d4a6f-6b34-4f02-b532-dcd7f3d5ae9d"
    },
    {
        "ChildrenId": [
            "1da84258-c62f-4bad-8a3c-9a975ed1c20c",
            "137d0b0e-8645-482d-be82-f450fe6307ea",
            "5d3d4a6f-6b34-4f02-b532-dcd7f3d5ae9d"
        ],
        "ChildrenName": [
            "standard deviation in li bond ionicity",
            "average li bond ionicity",
            "average bond ionicity of sublattice"
        ],
        "NodeName": "bond strength",
        "ParentId": "cd328a38-5a41-49bd-99a6-b92f758602ec",
        "Score": 0,
        "TreeType": "feature",
        "_id": "77f97fb4-ee17-4a81-8de7-8c09d4a7b772"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "bond length",
        "ParentId": "cd328a38-5a41-49bd-99a6-b92f758602ec",
        "Score": 0,
        "TreeType": "feature",
        "_id": "227ed0cc-e12a-46f8-863c-2ce044069674"
    },
    {
        "ChildrenId": [
            "77f97fb4-ee17-4a81-8de7-8c09d4a7b772",
            "227ed0cc-e12a-46f8-863c-2ce044069674"
        ],
        "ChildrenName": [
            "bond strength",
            "bond length"
        ],
        "NodeName": "interatomic parameter",
        "ParentId": "cf329d0d-2077-4962-b955-9a189e50f1bc",
        "Score": 0,
        "TreeType": "feature",
        "_id": "cd328a38-5a41-49bd-99a6-b92f758602ec"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "formation energy of competing phases",
        "ParentId": "46b56e14-856d-4ca2-99ac-f1f1fd8e39e1",
        "Score": 0,
        "TreeType": "feature",
        "_id": "06576001-e2cc-453a-94db-28213fd82dcf"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "ewald summation energy",
        "ParentId": "46b56e14-856d-4ca2-99ac-f1f1fd8e39e1",
        "Score": 0,
        "TreeType": "feature",
        "_id": "3465c341-fb31-4025-9fc3-cc3e96548498"
    },
    {
        "ChildrenId": [
            "06576001-e2cc-453a-94db-28213fd82dcf",
            "3465c341-fb31-4025-9fc3-cc3e96548498"
        ],
        "ChildrenName": [
            "formation energy of competing phases",
            "ewald summation energy"
        ],
        "NodeName": "energy",
        "ParentId": "38ed0641-813d-4cf0-93b2-bd531a49aeef",
        "Score": 0,
        "TreeType": "feature",
        "_id": "46b56e14-856d-4ca2-99ac-f1f1fd8e39e1"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "average electronegativity of sublattice",
        "ParentId": "e3453494-3b7c-43bb-b33f-59f36971f3e2",
        "Score": 0,
        "TreeType": "feature",
        "_id": "d73b8952-65f3-44a9-a9d4-757ef00163a3"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "average straight-line path electronegativity",
        "ParentId": "e3453494-3b7c-43bb-b33f-59f36971f3e2",
        "Score": 0,
        "TreeType": "feature",
        "_id": "7f14ba07-c7cd-4b45-9958-1c2563305733"
    },
    {
        "ChildrenId": [
            "d73b8952-65f3-44a9-a9d4-757ef00163a3",
            "7f14ba07-c7cd-4b45-9958-1c2563305733"
        ],
        "ChildrenName": [
            "average electronegativity of sublattice",
            "average straight-line path electronegativity"
        ],
        "NodeName": "electronegativity",
        "ParentId": "38ed0641-813d-4cf0-93b2-bd531a49aeef",
        "Score": 0,
        "TreeType": "feature",
        "_id": "e3453494-3b7c-43bb-b33f-59f36971f3e2"
    },
    {
        "ChildrenId": [
            "46b56e14-856d-4ca2-99ac-f1f1fd8e39e1",
            "e3453494-3b7c-43bb-b33f-59f36971f3e2"
        ],
        "ChildrenName": [
            "energy",
            "electronegativity"
        ],
        "NodeName": "overall parameters",
        "ParentId": "cf329d0d-2077-4962-b955-9a189e50f1bc",
        "Score": 0,
        "TreeType": "feature",
        "_id": "38ed0641-813d-4cf0-93b2-bd531a49aeef"
    },
    {
        "ChildrenId": [
            "bbd360da-3d6a-4cd2-be24-1bf7c8659689",
            "75fb3b22-ba16-4465-bfb0-3292c30c0426",
            "cd328a38-5a41-49bd-99a6-b92f758602ec",
            "38ed0641-813d-4cf0-93b2-bd531a49aeef"
        ],
        "ChildrenName": [
            "intrinsic-atomic parameter",
            "extrinsic-atomic parameter",
            "interatomic parameter",
            "overall parameters"
        ],
        "NodeName": "composition",
        "ParentId": "bbdcd985-c6dd-47d3-b2bb-9857dbad0ebf",
        "Score": 0,
        "TreeType": "feature",
        "_id": "cf329d0d-2077-4962-b955-9a189e50f1bc"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "a",
        "ParentId": "c9695b33-5a40-4160-b06f-add68bae0dea",
        "Score": 0,
        "TreeType": "feature",
        "_id": "de3a4ecc-a86e-4ab9-a4a9-99d1b3ac1749"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "c",
        "ParentId": "c9695b33-5a40-4160-b06f-add68bae0dea",
        "Score": 0,
        "TreeType": "feature",
        "_id": "7ce0e1f4-bb1a-4b88-ad77-ea76891451f6"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "a/c",
        "ParentId": "c9695b33-5a40-4160-b06f-add68bae0dea",
        "Score": 0,
        "TreeType": "feature",
        "_id": "e1d36edc-04b1-4a35-8466-65a51b7730fe"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "h",
        "ParentId": "c9695b33-5a40-4160-b06f-add68bae0dea",
        "Score": 0,
        "TreeType": "feature",
        "_id": "6403f6ea-33f6-4c8f-9d49-ca4b671a25e7"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "d",
        "ParentId": "c9695b33-5a40-4160-b06f-add68bae0dea",
        "Score": 0,
        "TreeType": "feature",
        "_id": "cc9b73ef-e410-4120-a566-6c2b8e1bcbbe"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "v",
        "ParentId": "c9695b33-5a40-4160-b06f-add68bae0dea",
        "Score": 0,
        "TreeType": "feature",
        "_id": "7c618121-981a-45da-ad67-8576ffffe525"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "lattice parameter a",
        "ParentId": "c9695b33-5a40-4160-b06f-add68bae0dea",
        "Score": 0,
        "TreeType": "feature",
        "_id": "f14caa46-e7ef-40b9-bcb5-9ac30474f560"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "lattice parameter c",
        "ParentId": "c9695b33-5a40-4160-b06f-add68bae0dea",
        "Score": 0,
        "TreeType": "feature",
        "_id": "6e2a2c6d-da05-4f62-8e8c-edaaed1cc061"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "lattice parameter v",
        "ParentId": "c9695b33-5a40-4160-b06f-add68bae0dea",
        "Score": 0,
        "TreeType": "feature",
        "_id": "ab7e0c70-c285-4c5d-bc92-45a42364b611"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "packing fraction of full crystal",
        "ParentId": "c9695b33-5a40-4160-b06f-add68bae0dea",
        "Score": 0,
        "TreeType": "feature",
        "_id": "f89d6432-7b4c-42ac-953d-914cfcf4d886"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "packing fraction of sublattice",
        "ParentId": "c9695b33-5a40-4160-b06f-add68bae0dea",
        "Score": 0,
        "TreeType": "feature",
        "_id": "9fc191b8-ae20-4139-86aa-b5a04abbe189"
    },
    {
        "ChildrenId": [
            "de3a4ecc-a86e-4ab9-a4a9-99d1b3ac1749",
            "7ce0e1f4-bb1a-4b88-ad77-ea76891451f6",
            "e1d36edc-04b1-4a35-8466-65a51b7730fe",
            "6403f6ea-33f6-4c8f-9d49-ca4b671a25e7",
            "cc9b73ef-e410-4120-a566-6c2b8e1bcbbe",
            "7c618121-981a-45da-ad67-8576ffffe525",
            "f14caa46-e7ef-40b9-bcb5-9ac30474f560",
            "6e2a2c6d-da05-4f62-8e8c-edaaed1cc061",
            "ab7e0c70-c285-4c5d-bc92-45a42364b611",
            "f89d6432-7b4c-42ac-953d-914cfcf4d886",
            "9fc191b8-ae20-4139-86aa-b5a04abbe189"
        ],
        "ChildrenName": [
            "a",
            "c",
            "a/c",
            "h",
            "d",
            "v",
            "lattice parameter a",
            "lattice parameter c",
            "lattice parameter v",
            "packing fraction of full crystal",
            "packing fraction of sublattice"
        ],
        "NodeName": "lattice parameters",
        "ParentId": "971db0bd-7593-4630-a3b7-b89f3da8cb43",
        "Score": 0,
        "TreeType": "feature",
        "_id": "c9695b33-5a40-4160-b06f-add68bae0dea"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "configurational entropy of na+ in 6b site",
        "ParentId": "3410020d-8ad0-481a-822d-cf28e3ca5bbd",
        "Score": 0,
        "TreeType": "feature",
        "_id": "6b78154d-1c50-4b8c-8d61-738c43c1627c"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "configurational entropy of na+ in 18e site",
        "ParentId": "3410020d-8ad0-481a-822d-cf28e3ca5bbd",
        "Score": 0,
        "TreeType": "feature",
        "_id": "911d5302-656e-4679-9642-c62d15079afc"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "configurational entropy of na+ in 36f site",
        "ParentId": "3410020d-8ad0-481a-822d-cf28e3ca5bbd",
        "Score": 0,
        "TreeType": "feature",
        "_id": "445348e3-0682-4d66-8190-bad2635a18fc"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "configurational entropy of na+",
        "ParentId": "3410020d-8ad0-481a-822d-cf28e3ca5bbd",
        "Score": 0,
        "TreeType": "feature",
        "_id": "3c7cc70e-f34b-431f-a68d-259d7cb8babd"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "configurational entropy of cationic in m site",
        "ParentId": "3410020d-8ad0-481a-822d-cf28e3ca5bbd",
        "Score": 0,
        "TreeType": "feature",
        "_id": "6ce39911-5bd0-4492-8b09-0eb9deab2f25"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "configurational entropy of cationic in x site",
        "ParentId": "3410020d-8ad0-481a-822d-cf28e3ca5bbd",
        "Score": 0,
        "TreeType": "feature",
        "_id": "62e46d4c-c610-4abc-9c9a-0068cbc61337"
    },
    {
        "ChildrenId": [
            "6b78154d-1c50-4b8c-8d61-738c43c1627c",
            "911d5302-656e-4679-9642-c62d15079afc",
            "445348e3-0682-4d66-8190-bad2635a18fc",
            "3c7cc70e-f34b-431f-a68d-259d7cb8babd",
            "6ce39911-5bd0-4492-8b09-0eb9deab2f25",
            "62e46d4c-c610-4abc-9c9a-0068cbc61337"
        ],
        "ChildrenName": [
            "configurational entropy of na+ in 6b site",
            "configurational entropy of na+ in 18e site",
            "configurational entropy of na+ in 36f site",
            "configurational entropy of na+",
            "configurational entropy of cationic in m site",
            "configurational entropy of cationic in x site"
        ],
        "NodeName": "structure disorder",
        "ParentId": "971db0bd-7593-4630-a3b7-b89f3da8cb43",
        "Score": 0,
        "TreeType": "feature",
        "_id": "3410020d-8ad0-481a-822d-cf28e3ca5bbd"
    },
    {
        "ChildrenId": [
            "c9695b33-5a40-4160-b06f-add68bae0dea",
            "3410020d-8ad0-481a-822d-cf28e3ca5bbd"
        ],
        "ChildrenName": [
            "lattice parameters",
            "structure disorder"
        ],
        "NodeName": "general structure",
        "ParentId": "5a115f3d-a5bf-431b-9b7f-8b2e7ae168f0",
        "Score": 0,
        "TreeType": "feature",
        "_id": "971db0bd-7593-4630-a3b7-b89f3da8cb43"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "standard deviation in li neighbor count",
        "ParentId": "67be4954-bd0d-42e4-a923-51b472ff2947",
        "Score": 0,
        "TreeType": "feature",
        "_id": "8f0ffe4b-b466-478d-9e9a-4915c806e954"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "average li neighbor count",
        "ParentId": "67be4954-bd0d-42e4-a923-51b472ff2947",
        "Score": 0,
        "TreeType": "feature",
        "_id": "8acc65d4-1610-41ab-b054-6246074171a7"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "average sublattice neighbor count",
        "ParentId": "67be4954-bd0d-42e4-a923-51b472ff2947",
        "Score": 0,
        "TreeType": "feature",
        "_id": "52c65964-e44b-4618-ba76-c5c1427dfec9"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "anion framework coordination",
        "ParentId": "67be4954-bd0d-42e4-a923-51b472ff2947",
        "Score": 0,
        "TreeType": "feature",
        "_id": "afb66935-27e2-4f1a-be35-da0ece28911f"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "average li-li bonds per li",
        "ParentId": "67be4954-bd0d-42e4-a923-51b472ff2947",
        "Score": 0,
        "TreeType": "feature",
        "_id": "f2868bc9-b5dd-4e82-9b26-1e25d9d18646"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "ratio of average li neighbor count to average sublattice neighbor count",
        "ParentId": "67be4954-bd0d-42e4-a923-51b472ff2947",
        "Score": 0,
        "TreeType": "feature",
        "_id": "fe75450a-7e43-4e89-8c92-cfa2eb83ba15"
    },
    {
        "ChildrenId": [
            "8f0ffe4b-b466-478d-9e9a-4915c806e954",
            "8acc65d4-1610-41ab-b054-6246074171a7",
            "52c65964-e44b-4618-ba76-c5c1427dfec9",
            "afb66935-27e2-4f1a-be35-da0ece28911f",
            "f2868bc9-b5dd-4e82-9b26-1e25d9d18646",
            "fe75450a-7e43-4e89-8c92-cfa2eb83ba15"
        ],
        "ChildrenName": [
            "standard deviation in li neighbor count",
            "average li neighbor count",
            "average sublattice neighbor count",
            "anion framework coordination",
            "average li-li bonds per li",
            "ratio of average li neighbor count to average sublattice neighbor count"
        ],
        "NodeName": "coordination",
        "ParentId": "b9c6daa1-2e69-47fc-a862-202f07258553",
        "Score": 0,
        "TreeType": "feature",
        "_id": "67be4954-bd0d-42e4-a923-51b472ff2947"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "volume of mo6  polyhedron",
        "ParentId": "0ca3b457-bba3-41ff-895b-ac4c89238152",
        "Score": 0,
        "TreeType": "feature",
        "_id": "bd654462-b3b4-4b51-b26d-fe1045954386"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "volume of xo4  polyhedron",
        "ParentId": "0ca3b457-bba3-41ff-895b-ac4c89238152",
        "Score": 0,
        "TreeType": "feature",
        "_id": "42909dd0-042a-42d2-8f38-c68e5400755e"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "volume of na1o6  polyhedron",
        "ParentId": "0ca3b457-bba3-41ff-895b-ac4c89238152",
        "Score": 0,
        "TreeType": "feature",
        "_id": "891db005-2374-4ffd-af86-058fc583d4c0"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "volume of na2o8  polyhedron",
        "ParentId": "0ca3b457-bba3-41ff-895b-ac4c89238152",
        "Score": 0,
        "TreeType": "feature",
        "_id": "58252553-b5f5-44ac-a3c8-da9bf0b3b8df"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "volume of na3o5  polyhedron",
        "ParentId": "0ca3b457-bba3-41ff-895b-ac4c89238152",
        "Score": 0,
        "TreeType": "feature",
        "_id": "0477645c-6ee2-40ea-a0dd-eb5fd332ee93"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "average atomic volume",
        "ParentId": "0ca3b457-bba3-41ff-895b-ac4c89238152",
        "Score": 0,
        "TreeType": "feature",
        "_id": "818221bd-1315-49fd-bdab-3bbaba14a7a6"
    },
    {
        "ChildrenId": [
            "bd654462-b3b4-4b51-b26d-fe1045954386",
            "42909dd0-042a-42d2-8f38-c68e5400755e",
            "891db005-2374-4ffd-af86-058fc583d4c0",
            "58252553-b5f5-44ac-a3c8-da9bf0b3b8df",
            "0477645c-6ee2-40ea-a0dd-eb5fd332ee93",
            "818221bd-1315-49fd-bdab-3bbaba14a7a6"
        ],
        "ChildrenName": [
            "volume of mo6  polyhedron",
            "volume of xo4  polyhedron",
            "volume of na1o6  polyhedron",
            "volume of na2o8  polyhedron",
            "volume of na3o5  polyhedron",
            "average atomic volume"
        ],
        "NodeName": "volume",
        "ParentId": "b9c6daa1-2e69-47fc-a862-202f07258553",
        "Score": 0,
        "TreeType": "feature",
        "_id": "0ca3b457-bba3-41ff-895b-ac4c89238152"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "minimum bottleneck of na+ jumps from 6b site to 36f site",
        "ParentId": "ab0c2b5b-4449-4bc4-be15-165f29301816",
        "Score": 0,
        "TreeType": "feature",
        "_id": "73afe7e0-84ba-4b55-b0ec-429ab4bd6c17"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "minimum bottleneck of na+ jumps from 18e site to 36f site",
        "ParentId": "ab0c2b5b-4449-4bc4-be15-165f29301816",
        "Score": 0,
        "TreeType": "feature",
        "_id": "7a9867eb-3412-490a-b662-3d543a5aab76"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "the minimum of bt2 and bt1",
        "ParentId": "ab0c2b5b-4449-4bc4-be15-165f29301816",
        "Score": 0,
        "TreeType": "feature",
        "_id": "ceba2b3b-929b-4343-954d-691921ed3773"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "radius of largest sphere probe that can freely pass through the void space packed by framework ions",
        "ParentId": "ab0c2b5b-4449-4bc4-be15-165f29301816",
        "Score": 0,
        "TreeType": "feature",
        "_id": "dbd8850c-b8ba-4515-98ed-b495212c171c"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "average straight-line path width",
        "ParentId": "ab0c2b5b-4449-4bc4-be15-165f29301816",
        "Score": 0,
        "TreeType": "feature",
        "_id": "f46f3be1-2cf0-4746-8dcc-668021820fb0"
    },
    {
        "ChildrenId": [
            "73afe7e0-84ba-4b55-b0ec-429ab4bd6c17",
            "7a9867eb-3412-490a-b662-3d543a5aab76",
            "ceba2b3b-929b-4343-954d-691921ed3773",
            "dbd8850c-b8ba-4515-98ed-b495212c171c",
            "f46f3be1-2cf0-4746-8dcc-668021820fb0"
        ],
        "ChildrenName": [
            "minimum bottleneck of na+ jumps from 6b site to 36f site",
            "minimum bottleneck of na+ jumps from 18e site to 36f site",
            "the minimum of bt2 and bt1",
            "radius of largest sphere probe that can freely pass through the void space packed by framework ions",
            "average straight-line path width"
        ],
        "NodeName": "bottleneck",
        "ParentId": "ae3bcc46-5987-432d-aeca-6426222db868",
        "Score": 0,
        "TreeType": "feature",
        "_id": "ab0c2b5b-4449-4bc4-be15-165f29301816"
    },
    {
        "ChildrenId": [
            "ab0c2b5b-4449-4bc4-be15-165f29301816"
        ],
        "ChildrenName": [
            "bottleneck"
        ],
        "NodeName": "channel",
        "ParentId": "b9c6daa1-2e69-47fc-a862-202f07258553",
        "Score": 0,
        "TreeType": "feature",
        "_id": "ae3bcc46-5987-432d-aeca-6426222db868"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "average shortest anion-anion separation distance",
        "ParentId": "cbff8c29-1b18-4d31-bdc3-4a338edac1c5",
        "Score": 0,
        "TreeType": "feature",
        "_id": "440a3781-32ff-42db-9f15-22d42f5ff728"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "average shortest li-anion separation distance",
        "ParentId": "cbff8c29-1b18-4d31-bdc3-4a338edac1c5",
        "Score": 0,
        "TreeType": "feature",
        "_id": "42697de6-0974-4e33-bd1c-59db93997f80"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "average shortest li-li separation distance",
        "ParentId": "cbff8c29-1b18-4d31-bdc3-4a338edac1c5",
        "Score": 0,
        "TreeType": "feature",
        "_id": "f907fa05-dd4a-4b1c-a208-2dcea4279d72"
    },
    {
        "ChildrenId": [
            "440a3781-32ff-42db-9f15-22d42f5ff728",
            "42697de6-0974-4e33-bd1c-59db93997f80",
            "f907fa05-dd4a-4b1c-a208-2dcea4279d72"
        ],
        "ChildrenName": [
            "average shortest anion-anion separation distance",
            "average shortest li-anion separation distance",
            "average shortest li-li separation distance"
        ],
        "NodeName": "distance",
        "ParentId": "b9c6daa1-2e69-47fc-a862-202f07258553",
        "Score": 0,
        "TreeType": "feature",
        "_id": "cbff8c29-1b18-4d31-bdc3-4a338edac1c5"
    },
    {
        "ChildrenId": [
            "67be4954-bd0d-42e4-a923-51b472ff2947",
            "0ca3b457-bba3-41ff-895b-ac4c89238152",
            "ae3bcc46-5987-432d-aeca-6426222db868",
            "cbff8c29-1b18-4d31-bdc3-4a338edac1c5"
        ],
        "ChildrenName": [
            "coordination",
            "volume",
            "channel",
            "distance"
        ],
        "NodeName": "local structure",
        "ParentId": "5a115f3d-a5bf-431b-9b7f-8b2e7ae168f0",
        "Score": 0,
        "TreeType": "feature",
        "_id": "b9c6daa1-2e69-47fc-a862-202f07258553"
    },
    {
        "ChildrenId": [
            "971db0bd-7593-4630-a3b7-b89f3da8cb43",
            "b9c6daa1-2e69-47fc-a862-202f07258553"
        ],
        "ChildrenName": [
            "general structure",
            "local structure"
        ],
        "NodeName": "structure",
        "ParentId": "bbdcd985-c6dd-47d3-b2bb-9857dbad0ebf",
        "Score": 0,
        "TreeType": "feature",
        "_id": "5a115f3d-a5bf-431b-9b7f-8b2e7ae168f0"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "preparation parameter",
        "ParentId": "cc4fc25f-63ea-4044-b742-e2a766a2d204",
        "Score": 0,
        "TreeType": "feature",
        "_id": "f7a765f3-d261-4333-96f3-d4c126d32466"
    },
    {
        "ChildrenId": [
            "f7a765f3-d261-4333-96f3-d4c126d32466"
        ],
        "ChildrenName": [
            "preparation parameter"
        ],
        "NodeName": "process",
        "ParentId": "bbdcd985-c6dd-47d3-b2bb-9857dbad0ebf",
        "Score": 0,
        "TreeType": "feature",
        "_id": "cc4fc25f-63ea-4044-b742-e2a766a2d204"
    },
    {
        "ChildrenId": [],
        "ChildrenName": [],
        "NodeName": "the temperature of the structure is measured",
        "ParentId": "a0c56487-4f67-41ba-9749-4a5f8f3cca8c",
        "Score": 0,
        "TreeType": "feature",
        "_id": "f92cd9f2-f60f-452b-9fbd-0107b89abcdd"
    },
    {
        "ChildrenId": [
            "f92cd9f2-f60f-452b-9fbd-0107b89abcdd"
        ],
        "ChildrenName": [
            "the temperature of the structure is measured"
        ],
        "NodeName": "characteristic parameter",
        "ParentId": "eca6521e-783d-4aa2-91ac-b705be306dbf",
        "Score": 0,
        "TreeType": "feature",
        "_id": "a0c56487-4f67-41ba-9749-4a5f8f3cca8c"
    },
    {
        "ChildrenId": [
            "a0c56487-4f67-41ba-9749-4a5f8f3cca8c"
        ],
        "ChildrenName": [
            "characteristic parameter"
        ],
        "NodeName": "condition",
        "ParentId": "bbdcd985-c6dd-47d3-b2bb-9857dbad0ebf",
        "Score": 0,
        "TreeType": "feature",
        "_id": "eca6521e-783d-4aa2-91ac-b705be306dbf"
    },
    {
        "ChildrenId": [
            "cf329d0d-2077-4962-b955-9a189e50f1bc",
            "5a115f3d-a5bf-431b-9b7f-8b2e7ae168f0",
            "cc4fc25f-63ea-4044-b742-e2a766a2d204",
            "eca6521e-783d-4aa2-91ac-b705be306dbf"
        ],
        "ChildrenName": [
            "composition",
            "structure",
            "process",
            "condition"
        ],
        "NodeName": "descriptors",
        "ParentId": "",
        "Score": 0,
        "TreeType": "feature",
        "_id": "bbdcd985-c6dd-47d3-b2bb-9857dbad0ebf"
    }
]'''

data = json.loads(json_data)

# 创建一个新的 CSV 文件
csv_file = open('data.csv', 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)

# 写入标题行
csv_writer.writerow(data[0].keys())

# 写入数据行
for item in data:
    csv_writer.writerow(item.values())

# 关闭 CSV 文件
csv_file.close()
