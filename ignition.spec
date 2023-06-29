%bcond_with check

%global dracutlibdir %{_prefix}/lib/dracut
%global gobuild go build 
%global gotest go test

Name:           ignition
Version:        2.14.0
Release:        3
Summary:        First boot installer and configuration tool
License:        Apache-2.0
URL:            https://github.com/coreos/ignition
Source0:        https://github.com/coreos/ignition/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         fix-clang.patch

BuildRequires: libblkid-devel
BuildRequires: golang >= 1.10
BuildRequires: systemd

# Requires for 'disks' stage
Recommends: btrfs-progs
Requires: dosfstools
Requires: gdisk
Requires: dracut
Requires: dracut-network

Obsoletes: ignition-dracut < 0.31.0-3

# Main package Provides (generated with go-mods-to-bundled-provides.py | sort)
Provides: bundled(golang(cloud.google.com/go)) = 0.58.0
Provides: bundled(golang(cloud.google.com/go/compute/metadata)) = 0.58.0
Provides: bundled(golang(cloud.google.com/go/iam)) = 0.58.0
Provides: bundled(golang(cloud.google.com/go/internal)) = 0.58.0
Provides: bundled(golang(cloud.google.com/go/internal/optional)) = 0.58.0
Provides: bundled(golang(cloud.google.com/go/internal/trace)) = 0.58.0
Provides: bundled(golang(cloud.google.com/go/internal/version)) = 0.58.0
Provides: bundled(golang(cloud.google.com/go/storage)) = 0.58.0
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws)) = 1.30.28
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/arn)) = 1.30.28
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/awserr)) = 1.30.28
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/awsutil)) = 1.30.28
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/client)) = 1.30.28
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/client/metadata)) = 1.30.28
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/corehandlers)) = 1.30.28
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/credentials)) = 1.30.28
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/credentials/ec2rolecreds)) = 1.30.28
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/credentials/endpointcreds)) = 1.30.28
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/credentials/processcreds)) = 1.30.28
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/credentials/stscreds)) = 1.30.28
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/csm)) = 1.30.28
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/defaults)) = 1.30.28
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/ec2metadata)) = 1.30.28
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/endpoints)) = 1.30.28
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/request)) = 1.30.28
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/session)) = 1.30.28
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/signer/v4)) = 1.30.28
Provides: bundled(golang(github.com/aws/aws-sdk-go/internal/context)) = 1.30.28
Provides: bundled(golang(github.com/aws/aws-sdk-go/internal/ini)) = 1.30.28
Provides: bundled(golang(github.com/aws/aws-sdk-go/internal/s3err)) = 1.30.28
Provides: bundled(golang(github.com/aws/aws-sdk-go/internal/sdkio)) = 1.30.28
Provides: bundled(golang(github.com/aws/aws-sdk-go/internal/sdkmath)) = 1.30.28
Provides: bundled(golang(github.com/aws/aws-sdk-go/internal/sdkrand)) = 1.30.28
Provides: bundled(golang(github.com/aws/aws-sdk-go/internal/sdkuri)) = 1.30.28
Provides: bundled(golang(github.com/aws/aws-sdk-go/internal/shareddefaults)) = 1.30.28
Provides: bundled(golang(github.com/aws/aws-sdk-go/internal/strings)) = 1.30.28
Provides: bundled(golang(github.com/aws/aws-sdk-go/internal/sync/singleflight)) = 1.30.28
Provides: bundled(golang(github.com/aws/aws-sdk-go/private/protocol)) = 1.30.28
Provides: bundled(golang(github.com/aws/aws-sdk-go/private/protocol/eventstream)) = 1.30.28
Provides: bundled(golang(github.com/aws/aws-sdk-go/private/protocol/eventstream/eventstreamapi)) = 1.30.28
Provides: bundled(golang(github.com/aws/aws-sdk-go/private/protocol/json/jsonutil)) = 1.30.28
Provides: bundled(golang(github.com/aws/aws-sdk-go/private/protocol/query)) = 1.30.28
Provides: bundled(golang(github.com/aws/aws-sdk-go/private/protocol/query/queryutil)) = 1.30.28
Provides: bundled(golang(github.com/aws/aws-sdk-go/private/protocol/rest)) = 1.30.28
Provides: bundled(golang(github.com/aws/aws-sdk-go/private/protocol/restxml)) = 1.30.28
Provides: bundled(golang(github.com/aws/aws-sdk-go/private/protocol/xml/xmlutil)) = 1.30.28
Provides: bundled(golang(github.com/aws/aws-sdk-go/service/s3)) = 1.30.28
Provides: bundled(golang(github.com/aws/aws-sdk-go/service/s3/internal/arn)) = 1.30.28
Provides: bundled(golang(github.com/aws/aws-sdk-go/service/s3/s3iface)) = 1.30.28
Provides: bundled(golang(github.com/aws/aws-sdk-go/service/s3/s3manager)) = 1.30.28
Provides: bundled(golang(github.com/aws/aws-sdk-go/service/sts)) = 1.30.28
Provides: bundled(golang(github.com/aws/aws-sdk-go/service/sts/stsiface)) = 1.30.28
Provides: bundled(golang(github.com/beevik/etree)) = 1.1.1-0.20200718192613.git4a2f8b9d084c
Provides: bundled(golang(github.com/coreos/go-semver/semver)) = 0.3.0
Provides: bundled(golang(github.com/coreos/go-systemd/v22/dbus)) = 22.0.0
Provides: bundled(golang(github.com/coreos/go-systemd/v22/journal)) = 22.0.0
Provides: bundled(golang(github.com/coreos/go-systemd/v22/unit)) = 22.0.0
Provides: bundled(golang(github.com/coreos/vcontext/json)) = 0.0.0-20211021162308.gitf1dbbca7bef4
Provides: bundled(golang(github.com/coreos/vcontext/path)) = 0.0.0-20211021162308.gitf1dbbca7bef4
Provides: bundled(golang(github.com/coreos/vcontext/report)) = 0.0.0-20211021162308.gitf1dbbca7bef4
Provides: bundled(golang(github.com/coreos/vcontext/tree)) = 0.0.0-20211021162308.gitf1dbbca7bef4
Provides: bundled(golang(github.com/coreos/vcontext/validate)) = 0.0.0-20211021162308.gitf1dbbca7bef4
Provides: bundled(golang(github.com/google/renameio)) = 0.1.0
Provides: bundled(golang(github.com/google/uuid)) = 1.1.1
Provides: bundled(golang(github.com/pin/tftp)) = 2.1.0
Provides: bundled(golang(github.com/pin/tftp/netascii)) = 2.1.0
Provides: bundled(golang(github.com/spf13/pflag)) = 1.0.6-0.20210604193023.gitd5e0c0615ace
Provides: bundled(golang(github.com/stretchr/testify/assert)) = 1.7.0
Provides: bundled(golang(github.com/vincent-petithory/dataurl)) = 1.0.0
Provides: bundled(golang(github.com/vmware/vmw-guestinfo/bdoor)) = 0.0.0-20220317130741.git510905f0efa3
Provides: bundled(golang(github.com/vmware/vmw-guestinfo/message)) = 0.0.0-20220317130741.git510905f0efa3
Provides: bundled(golang(github.com/vmware/vmw-guestinfo/rpcout)) = 0.0.0-20220317130741.git510905f0efa3
Provides: bundled(golang(github.com/vmware/vmw-guestinfo/rpcvmx)) = 0.0.0-20220317130741.git510905f0efa3
Provides: bundled(golang(github.com/vmware/vmw-guestinfo/vmcheck)) = 0.0.0-20220317130741.git510905f0efa3
Provides: bundled(golang(golang.org/x/net/context)) = 0.0.0-20200602114024.git627f9648deb9
Provides: bundled(golang(golang.org/x/net/context/ctxhttp)) = 0.0.0-20200602114024.git627f9648deb9
Provides: bundled(golang(golang.org/x/net/http2)) = 0.0.0-20200602114024.git627f9648deb9
Provides: bundled(golang(golang.org/x/net/http2/hpack)) = 0.0.0-20200602114024.git627f9648deb9
Provides: bundled(golang(golang.org/x/net/http/httpguts)) = 0.0.0-20200602114024.git627f9648deb9
Provides: bundled(golang(golang.org/x/net/http/httpproxy)) = 0.0.0-20200602114024.git627f9648deb9
Provides: bundled(golang(golang.org/x/net/idna)) = 0.0.0-20200602114024.git627f9648deb9
Provides: bundled(golang(golang.org/x/net/internal/timeseries)) = 0.0.0-20200602114024.git627f9648deb9
Provides: bundled(golang(golang.org/x/net/trace)) = 0.0.0-20200602114024.git627f9648deb9
Provides: bundled(golang(golang.org/x/oauth2)) = 0.0.0-20200107190931.gitbf48bf16ab8d
Provides: bundled(golang(golang.org/x/oauth2/google)) = 0.0.0-20200107190931.gitbf48bf16ab8d
Provides: bundled(golang(golang.org/x/oauth2/internal)) = 0.0.0-20200107190931.gitbf48bf16ab8d
Provides: bundled(golang(golang.org/x/oauth2/jws)) = 0.0.0-20200107190931.gitbf48bf16ab8d
Provides: bundled(golang(golang.org/x/oauth2/jwt)) = 0.0.0-20200107190931.gitbf48bf16ab8d
Provides: bundled(golang(golang.org/x/sys/internal/unsafeheader)) = 0.0.0-20200610111108.git226ff32320da
Provides: bundled(golang(golang.org/x/sys/unix)) = 0.0.0-20200610111108.git226ff32320da
Provides: bundled(golang(golang.org/x/tools/cmd/goimports)) = 0.0.0-20200610160956.git3e83d1e96d0e
Provides: bundled(golang(golang.org/x/tools/go/analysis)) = 0.0.0-20200610160956.git3e83d1e96d0e
Provides: bundled(golang(golang.org/x/tools/go/analysis/passes/inspect)) = 0.0.0-20200610160956.git3e83d1e96d0e
Provides: bundled(golang(golang.org/x/tools/go/ast/astutil)) = 0.0.0-20200610160956.git3e83d1e96d0e
Provides: bundled(golang(golang.org/x/tools/go/ast/inspector)) = 0.0.0-20200610160956.git3e83d1e96d0e
Provides: bundled(golang(golang.org/x/tools/go/buildutil)) = 0.0.0-20200610160956.git3e83d1e96d0e
Provides: bundled(golang(golang.org/x/tools/go/gcexportdata)) = 0.0.0-20200610160956.git3e83d1e96d0e
Provides: bundled(golang(golang.org/x/tools/go/internal/cgo)) = 0.0.0-20200610160956.git3e83d1e96d0e
Provides: bundled(golang(golang.org/x/tools/go/internal/gcimporter)) = 0.0.0-20200610160956.git3e83d1e96d0e
Provides: bundled(golang(golang.org/x/tools/go/internal/packagesdriver)) = 0.0.0-20200610160956.git3e83d1e96d0e
Provides: bundled(golang(golang.org/x/tools/go/loader)) = 0.0.0-20200610160956.git3e83d1e96d0e
Provides: bundled(golang(golang.org/x/tools/go/packages)) = 0.0.0-20200610160956.git3e83d1e96d0e
Provides: bundled(golang(golang.org/x/tools/go/types/objectpath)) = 0.0.0-20200610160956.git3e83d1e96d0e
Provides: bundled(golang(golang.org/x/tools/go/types/typeutil)) = 0.0.0-20200610160956.git3e83d1e96d0e
Provides: bundled(golang(golang.org/x/tools/internal/analysisinternal)) = 0.0.0-20200610160956.git3e83d1e96d0e
Provides: bundled(golang(golang.org/x/tools/internal/event)) = 0.0.0-20200610160956.git3e83d1e96d0e
Provides: bundled(golang(golang.org/x/tools/internal/event/core)) = 0.0.0-20200610160956.git3e83d1e96d0e
Provides: bundled(golang(golang.org/x/tools/internal/event/keys)) = 0.0.0-20200610160956.git3e83d1e96d0e
Provides: bundled(golang(golang.org/x/tools/internal/event/label)) = 0.0.0-20200610160956.git3e83d1e96d0e
Provides: bundled(golang(golang.org/x/tools/internal/fastwalk)) = 0.0.0-20200610160956.git3e83d1e96d0e
Provides: bundled(golang(golang.org/x/tools/internal/gocommand)) = 0.0.0-20200610160956.git3e83d1e96d0e
Provides: bundled(golang(golang.org/x/tools/internal/gopathwalk)) = 0.0.0-20200610160956.git3e83d1e96d0e
Provides: bundled(golang(golang.org/x/tools/internal/imports)) = 0.0.0-20200610160956.git3e83d1e96d0e
Provides: bundled(golang(golang.org/x/tools/internal/packagesinternal)) = 0.0.0-20200610160956.git3e83d1e96d0e
Provides: bundled(golang(google.golang.org/api/googleapi)) = 0.26.0
Provides: bundled(golang(google.golang.org/api/googleapi/transport)) = 0.26.0
Provides: bundled(golang(google.golang.org/api/internal)) = 0.26.0
Provides: bundled(golang(google.golang.org/api/internal/gensupport)) = 0.26.0
Provides: bundled(golang(google.golang.org/api/internal/third_party/uritemplates)) = 0.26.0
Provides: bundled(golang(google.golang.org/api/iterator)) = 0.26.0
Provides: bundled(golang(google.golang.org/api/option)) = 0.26.0
Provides: bundled(golang(google.golang.org/api/option/internaloption)) = 0.26.0
Provides: bundled(golang(google.golang.org/api/storage/v1)) = 0.26.0
Provides: bundled(golang(google.golang.org/api/transport/cert)) = 0.26.0
Provides: bundled(golang(google.golang.org/api/transport/http)) = 0.26.0
Provides: bundled(golang(google.golang.org/api/transport/http/internal/propagation)) = 0.26.0
Provides: bundled(golang(google.golang.org/genproto/googleapis/api/annotations)) = 0.0.0-20200610104632.gita5b850bcf112
Provides: bundled(golang(google.golang.org/genproto/googleapis/iam/v1)) = 0.0.0-20200610104632.gita5b850bcf112
Provides: bundled(golang(google.golang.org/genproto/googleapis/rpc/code)) = 0.0.0-20200610104632.gita5b850bcf112
Provides: bundled(golang(google.golang.org/genproto/googleapis/rpc/status)) = 0.0.0-20200610104632.gita5b850bcf112
Provides: bundled(golang(google.golang.org/genproto/googleapis/type/expr)) = 0.0.0-20200610104632.gita5b850bcf112
Provides: bundled(golang(go.opencensus.io)) = 0.22.5
Provides: bundled(golang(go.opencensus.io/internal)) = 0.22.5
Provides: bundled(golang(go.opencensus.io/internal/tagencoding)) = 0.22.5
Provides: bundled(golang(go.opencensus.io/metric/metricdata)) = 0.22.5
Provides: bundled(golang(go.opencensus.io/metric/metricproducer)) = 0.22.5
Provides: bundled(golang(go.opencensus.io/plugin/ochttp)) = 0.22.5
Provides: bundled(golang(go.opencensus.io/plugin/ochttp/propagation/b3)) = 0.22.5
Provides: bundled(golang(go.opencensus.io/resource)) = 0.22.5
Provides: bundled(golang(go.opencensus.io/stats)) = 0.22.5
Provides: bundled(golang(go.opencensus.io/stats/internal)) = 0.22.5
Provides: bundled(golang(go.opencensus.io/stats/view)) = 0.22.5
Provides: bundled(golang(go.opencensus.io/tag)) = 0.22.5
Provides: bundled(golang(go.opencensus.io/trace)) = 0.22.5
Provides: bundled(golang(go.opencensus.io/trace/internal)) = 0.22.5
Provides: bundled(golang(go.opencensus.io/trace/propagation)) = 0.22.5
Provides: bundled(golang(go.opencensus.io/trace/tracestate)) = 0.22.5

%description
Ignition is a utility used to manipulate systems during the initramfs.
This includes partitioning disks, formatting partitions, writing files
(regular files, systemd units, etc.), and configuring users. On first
boot, Ignition reads its configuration from a source of truth (remote
URL, network metadata service, hypervisor bridge, etc.) and applies
the configuration.

############## validate subpackage ##############

%package validate
Summary:       Validation tool for Ignition configs
License:       Apache-2.0

Conflicts: ignition < 0.31.0-3

%description validate
Ignition is a utility used to manipulate systems during the initramfs.
This includes partitioning disks, formatting partitions, writing files
(regular files, systemd units, etc.), and configuring users. On first
boot, Ignition reads its configuration from a source of truth (remote
URL, network metadata service, hypervisor bridge, etc.) and applies
the configuration.
This package contains a tool for validating Ignition configurations.

%prep
%autosetup -p1

%build
export LDFLAGS="-X github.com/coreos/ignition/v2/internal/version.Raw=%{version} -X github.com/coreos/ignition/v2/internal/distro.selinuxRelabel=true "

# Modules
export GO111MODULE=on
export GOFLAGS="-mod=vendor"

echo "Building ignition..."
%gobuild -o ./ignition internal/main.go

echo "Building ignition-validate..."
%gobuild -o ./ignition-validate validate/main.go

%install
# dracut modules
install -d -p %{buildroot}/%{dracutlibdir}/modules.d
cp -r dracut/* %{buildroot}/%{dracutlibdir}/modules.d/
install -m 0644 -D -t %{buildroot}/%{_unitdir} systemd/ignition-delete-config.service
install -m 0755 -d %{buildroot}/%{_libexecdir}
ln -sf ../lib/dracut/modules.d/30ignition/ignition %{buildroot}/%{_libexecdir}/ignition-apply
ln -sf ../lib/dracut/modules.d/30ignition/ignition %{buildroot}/%{_libexecdir}/ignition-rmcfg

# ignition
install -d -p %{buildroot}%{_bindir}
install -p -m 0755 ./ignition-validate %{buildroot}%{_bindir}

# The ignition binary is only for dracut, and is dangerous to run from
# the command line.  Install directly into the dracut module dir.
install -p -m 0755 ./ignition %{buildroot}/%{dracutlibdir}/modules.d/30ignition

%if %{with check}
%check
# Exclude the blackbox tests
%gotest github.com/coreos/ignition/v2/tests
%endif

%files
%license LICENSE
%doc README.md docs/
%{dracutlibdir}/modules.d/*
%{_unitdir}/*.service
%{_libexecdir}/ignition-apply
%{_libexecdir}/ignition-rmcfg

%files validate
%doc README.md
%license LICENSE
%{_bindir}/ignition-validate

%changelog
* Tue Jun 27 2023 yoo <sunyuechi@iscas.ac.cn> - 2.14.0-3
- fix clang build error

* Wed Jan 04 2023 liukuo <liukuo@kylinos.cn> - 2.14.0-2
- Fix %{_unitdir} not identified

* Fri May 27 2022 duyiwei <duyiwei@kylinos.cn> - 2.14.0-1
- update version to 2.14.0
- fix CVE-2022-1706

* Mon May 23 2022 duyiwei <duyiwei@kylinos.cn> - 2.13.0-1
- update version to 2.13.0

* Fri Dec 24 2021 duyiwei <duyiwei@kylinos.cn> - 2.9.0-1
- Package init
