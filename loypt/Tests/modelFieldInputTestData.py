import datetime

vendor1TestData = {
    "shortDescription": "this is test vendor1",
    "longDescription": "this is test vendor1 description long version",
    "addressDetails": "this is new test address1",
    "pincode": "674821",
    "state": "teststate1",
    "contactNo": "9993872459",
}

vendor2TestData = {
    "shortDescription": "this is test vendor2",
    "longDescription": "this is test vendor2 description long version",
    "addressDetails": "this is new test address2",
    "pincode": "674821",
    "state": "teststate2",
    "contactNo": "9993892829",
}

user1TestData = {
    "username": "testuser1",
    "email": "testuser1@test.com",
    "password": "jdnvdp3904umeegeg",
}

user2TestData = {
    "username": "testuser2",
    "email": "testuser2@test.com",
    "password": "jdnvdp3904ume3egeg",
}

consumer1TestData = {
    "contactNo": "9993872811",
    "secondaryContactNo": "9993872822",
    "pointBal": 0,
}

consumer2TestData = {
    "contactNo": "9993872431",
    "secondaryContactNo": "9993572822",
    "pointBal": 0,
}


purchaseReg1TestData = {
    "purchaseRef": "o20fmw9v2r3pmfpf",
    "amount": 100.00,
}

purchaseReg2TestData = {
    "purchaseRef": "mw0ms0204820wdkdis",
    "amount": 70.00,
}

catalogue1TestData = {
    "code": "NEWUSER1",
    "percentFromPurchVal": 10.0,
    "IsPointCap": True,
    "capPerOrder": 100,
    "capTimeLine": datetime.date.today() + datetime.timedelta(days=100),
    "campaignName": "New Test Campaign1",
    "campaignStartDate": datetime.date.today(),
    "campaignEndDate": datetime.date.today() + datetime.timedelta(days=30),
    "pointEffectiveDate": datetime.date.today(),
    "pointExpiryDate": datetime.date.today() + datetime.timedelta(days=50),
    "noOfTargetCustomers": 500,
}

catalogue2TestData = {
    "code": "NEWUSER2",
    "percentFromPurchVal": 20.00,
    "IsPointCap": True,
    "capPerOrder": 50,
    "capTimeLine": datetime.date.today() + datetime.timedelta(days=30),
    "campaignName": "New Test Campaign2",
    "campaignStartDate": datetime.date.today(),
    "campaignEndDate": datetime.date.today() + datetime.timedelta(days=28),
    "pointEffectiveDate": datetime.date.today(),
    "pointExpiryDate": datetime.date.today() + datetime.timedelta(days=100),
    "noOfTargetCustomers": 250,
}

walletPoint1TestData = {
    "preBal": 0.0,
    "newBal": 10.0,
    "points": 10.0,
    "expiry": datetime.datetime.now(datetime.timezone.utc)
    + datetime.timedelta(days=50, hours=1, minutes=30),
}

walletPoint2TestData = {
    "preBal": 0.0,
    "newBal": 14.0,
    "points": 14.0,
    "expiry": datetime.datetime.now(datetime.timezone.utc)
    + datetime.timedelta(days=100, hours=1, minutes=30),
}
