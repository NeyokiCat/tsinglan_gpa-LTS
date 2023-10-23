import os

settings = {
    "host": os.environ.get(
        "ACCOUNT_HOST", "https://gaoyan2.documents.azure.com:443/"
    ),
    "master_key": os.environ.get(
        "ACCOUNT_KEY",
        "tHxrpRb8Z6U5ryFm2bs6IR6YgL32OMQcBw57UczIdev77uIZf2ZFK3XphlCERrTGOCrNAUsosBonACDbxbW5Hg==",
    ),
    "database_prefix": os.environ.get("COSMOS_DATABASE_PREFIX", "Master_"),
    "container_prefix": os.environ.get("COSMOS_CONTAINER", "Sub_"),
    "mode": os.environ.get("MODE", "blacklist"),
    "onhold_threshold": os.environ.get("ONHOLD_THRESHOLD", 5),
    "normal_limit": os.environ.get("NORMAL_LIMIT", 10),
    "onhold_limit": os.environ.get("ONHOLD_LIMIT", 2),
    "suffix": os.environ.get("SUFFIX", "gy"),
    "enc_key": os.environ.get("ENCRYPTION_KEY", "+62ALFe!U8jf74KPVRvy9(HWN8+kjMyVU4FW#^UeywzEJGZXr5PrtPC$n%&zUcE3"),
    "server_host": os.environ.get("SERVER_HOSTNAME", "gpa_tls.marksong.tech"),
}
