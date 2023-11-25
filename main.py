def rsshub(url: str) -> str:
    if "zhihu.com" in url:
        return "https://rsshub.rssforever.com/zhihu/people/activities/{}".format(url.split("/")[-1])
    else:
        return "unrecognized url"


if __name__ == '__main__':
    url = input()
    print(rsshub(url))

