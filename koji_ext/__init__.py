import koji


def latest_build_info(session, search_result, arch):
    pkg_name = search_result['name']
    pkg_id = search_result['id']

    print(f"Package name: {pkg_name}")
    builds = session.listBuilds(pkg_id, state=1)
    latest = max(builds, key=lambda i: i['build_id'])
    latest_rpms = session.listBuildRPMs(latest['build_id'])
    result = list(filter(lambda b: b['arch'] == arch, latest_rpms))

    if not result:
        print(f'No builds found for {arch}, switching to "noarch"')
        arch = 'noarch'
        result = filter(lambda b: b['arch'] == arch, latest_rpms)

    print(f'\nBuild list for "{arch}":')
    print("===========================")
    for i in result:
        print(i['name'])


def search(tag, arch):
    session = koji.ClientSession("https://koji.fedoraproject.org/kojihub")
    search_results = session.search(tag, 'package', 'glob')

    if search_results:
        for result in search_results:
            latest_build_info(session, result, arch)
    else:
        print(f"Package: {tag} not found!")
