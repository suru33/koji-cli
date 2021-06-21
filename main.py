import koji

tag = "ImageMagick"
arch = 'aarch64'

session = koji.ClientSession("https://koji.fedoraproject.org/kojihub")
search_results = session.search(tag, 'package', 'glob')


def latest_build_info(search_result):
    pkg_name = search_result['name']
    pkg_id = search_result['id']

    print(f"Package name: {pkg_name}")
    builds = session.listBuilds(pkg_id, state=1)
    latest = max(builds, key=lambda i: i['build_id'])
    latest_rpms = session.listBuildRPMs(latest['build_id'])
    result = filter(lambda b: b['arch'] == arch, latest_rpms)

    if not result:
        result = filter(lambda b: b['arch'] == 'src', latest_rpms)

    for i in result:
        print(i['name'])


if search_results:
    for r in search_results:
        latest_build_info(r)
else:
    print(f"Package: {tag} not found!")
