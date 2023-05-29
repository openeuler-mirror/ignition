%bcond_with check

%global dracutlibdir %{_prefix}/lib/dracut
%global gobuild go build 
%global gotest go test

Name:           ignition
Version:        2.15.0
Release:        1
Summary:        First boot installer and configuration tool
License:        Apache-2.0
URL:            https://github.com/coreos/ignition
Source0:        https://github.com/coreos/ignition/archive/v%{version}/%{name}-%{version}.tar.gz

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
Provides: bundled(golang(cloud.google.com/go/compute/metadata)) = 0.2.3
Provides: bundled(golang(cloud.google.com/go/storage)) = 1.29.0
Provides: bundled(golang(cloud.google.com/go/storage/internal)) = 1.29.0
Provides: bundled(golang(cloud.google.com/go/storage/internal/apiv2)) = 1.29.0
Provides: bundled(golang(cloud.google.com/go/storage/internal/apiv2/stubs)) = 1.29.0
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws)) = 1.44.204
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/arn)) = 1.44.204
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/awserr)) = 1.44.204
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/awsutil)) = 1.44.204
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/client)) = 1.44.204
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/client/metadata)) = 1.44.204
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/corehandlers)) = 1.44.204
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/credentials)) = 1.44.204
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/credentials/ec2rolecreds)) = 1.44.204
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/credentials/endpointcreds)) = 1.44.204
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/credentials/processcreds)) = 1.44.204
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/credentials/ssocreds)) = 1.44.204
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/credentials/stscreds)) = 1.44.204
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/csm)) = 1.44.204
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/defaults)) = 1.44.204
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/ec2metadata)) = 1.44.204
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/endpoints)) = 1.44.204
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/request)) = 1.44.204
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/session)) = 1.44.204
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/signer/v4)) = 1.44.204
Provides: bundled(golang(github.com/aws/aws-sdk-go/internal/context)) = 1.44.204
Provides: bundled(golang(github.com/aws/aws-sdk-go/internal/ini)) = 1.44.204
Provides: bundled(golang(github.com/aws/aws-sdk-go/internal/s3shared)) = 1.44.204
Provides: bundled(golang(github.com/aws/aws-sdk-go/internal/s3shared/arn)) = 1.44.204
Provides: bundled(golang(github.com/aws/aws-sdk-go/internal/s3shared/s3err)) = 1.44.204
Provides: bundled(golang(github.com/aws/aws-sdk-go/internal/sdkio)) = 1.44.204
Provides: bundled(golang(github.com/aws/aws-sdk-go/internal/sdkmath)) = 1.44.204
Provides: bundled(golang(github.com/aws/aws-sdk-go/internal/sdkrand)) = 1.44.204
Provides: bundled(golang(github.com/aws/aws-sdk-go/internal/sdkuri)) = 1.44.204
Provides: bundled(golang(github.com/aws/aws-sdk-go/internal/shareddefaults)) = 1.44.204
Provides: bundled(golang(github.com/aws/aws-sdk-go/internal/strings)) = 1.44.204
Provides: bundled(golang(github.com/aws/aws-sdk-go/internal/sync/singleflight)) = 1.44.204
Provides: bundled(golang(github.com/aws/aws-sdk-go/private/checksum)) = 1.44.204
Provides: bundled(golang(github.com/aws/aws-sdk-go/private/protocol)) = 1.44.204
Provides: bundled(golang(github.com/aws/aws-sdk-go/private/protocol/eventstream)) = 1.44.204
Provides: bundled(golang(github.com/aws/aws-sdk-go/private/protocol/eventstream/eventstreamapi)) = 1.44.204
Provides: bundled(golang(github.com/aws/aws-sdk-go/private/protocol/json/jsonutil)) = 1.44.204
Provides: bundled(golang(github.com/aws/aws-sdk-go/private/protocol/jsonrpc)) = 1.44.204
Provides: bundled(golang(github.com/aws/aws-sdk-go/private/protocol/query)) = 1.44.204
Provides: bundled(golang(github.com/aws/aws-sdk-go/private/protocol/query/queryutil)) = 1.44.204
Provides: bundled(golang(github.com/aws/aws-sdk-go/private/protocol/rest)) = 1.44.204
Provides: bundled(golang(github.com/aws/aws-sdk-go/private/protocol/restjson)) = 1.44.204
Provides: bundled(golang(github.com/aws/aws-sdk-go/private/protocol/restxml)) = 1.44.204
Provides: bundled(golang(github.com/aws/aws-sdk-go/private/protocol/xml/xmlutil)) = 1.44.204
Provides: bundled(golang(github.com/aws/aws-sdk-go/service/s3)) = 1.44.204
Provides: bundled(golang(github.com/aws/aws-sdk-go/service/s3/s3iface)) = 1.44.204
Provides: bundled(golang(github.com/aws/aws-sdk-go/service/s3/s3manager)) = 1.44.204
Provides: bundled(golang(github.com/aws/aws-sdk-go/service/sso)) = 1.44.204
Provides: bundled(golang(github.com/aws/aws-sdk-go/service/sso/ssoiface)) = 1.44.204
Provides: bundled(golang(github.com/aws/aws-sdk-go/service/sts)) = 1.44.204
Provides: bundled(golang(github.com/aws/aws-sdk-go/service/sts/stsiface)) = 1.44.204
Provides: bundled(golang(github.com/beevik/etree)) = 1.1.1-0.20200718192613.git4a2f8b9d084c
Provides: bundled(golang(github.com/coreos/go-semver/semver)) = 0.3.1
Provides: bundled(golang(github.com/coreos/go-systemd/v22/dbus)) = 22.5.0
Provides: bundled(golang(github.com/coreos/go-systemd/v22/journal)) = 22.5.0
Provides: bundled(golang(github.com/coreos/go-systemd/v22/unit)) = 22.5.0
Provides: bundled(golang(github.com/coreos/vcontext/json)) = 0.0.0-20230201181013.gitd72178a18687
Provides: bundled(golang(github.com/coreos/vcontext/path)) = 0.0.0-20230201181013.gitd72178a18687
Provides: bundled(golang(github.com/coreos/vcontext/report)) = 0.0.0-20230201181013.gitd72178a18687
Provides: bundled(golang(github.com/coreos/vcontext/tree)) = 0.0.0-20230201181013.gitd72178a18687
Provides: bundled(golang(github.com/coreos/vcontext/validate)) = 0.0.0-20230201181013.gitd72178a18687
Provides: bundled(golang(github.com/google/renameio/v2)) = 2.0.0
Provides: bundled(golang(github.com/google/uuid)) = 1.3.0
Provides: bundled(golang(github.com/pin/tftp)) = 2.1.0
Provides: bundled(golang(github.com/pin/tftp/netascii)) = 2.1.0
Provides: bundled(golang(github.com/spf13/pflag)) = 1.0.6-0.20210604193023.gitd5e0c0615ace
Provides: bundled(golang(github.com/stretchr/testify/assert)) = 1.8.1
Provides: bundled(golang(github.com/vincent-petithory/dataurl)) = 1.0.0
Provides: bundled(golang(github.com/vmware/vmw-guestinfo/bdoor)) = 0.0.0-20220317130741.git510905f0efa3
Provides: bundled(golang(github.com/vmware/vmw-guestinfo/message)) = 0.0.0-20220317130741.git510905f0efa3
Provides: bundled(golang(github.com/vmware/vmw-guestinfo/rpcout)) = 0.0.0-20220317130741.git510905f0efa3
Provides: bundled(golang(github.com/vmware/vmw-guestinfo/rpcvmx)) = 0.0.0-20220317130741.git510905f0efa3
Provides: bundled(golang(github.com/vmware/vmw-guestinfo/vmcheck)) = 0.0.0-20220317130741.git510905f0efa3
Provides: bundled(golang(golang.org/x/net/context)) = 0.7.0
Provides: bundled(golang(golang.org/x/net/http2)) = 0.7.0
Provides: bundled(golang(golang.org/x/net/http2/hpack)) = 0.7.0
Provides: bundled(golang(golang.org/x/net/http/httpguts)) = 0.7.0
Provides: bundled(golang(golang.org/x/net/http/httpproxy)) = 0.7.0
Provides: bundled(golang(golang.org/x/net/idna)) = 0.7.0
Provides: bundled(golang(golang.org/x/net/internal/timeseries)) = 0.7.0
Provides: bundled(golang(golang.org/x/net/trace)) = 0.7.0
Provides: bundled(golang(golang.org/x/oauth2)) = 0.5.0
Provides: bundled(golang(golang.org/x/oauth2/authhandler)) = 0.5.0
Provides: bundled(golang(golang.org/x/oauth2/google)) = 0.5.0
Provides: bundled(golang(golang.org/x/oauth2/google/internal/externalaccount)) = 0.5.0
Provides: bundled(golang(golang.org/x/oauth2/internal)) = 0.5.0
Provides: bundled(golang(golang.org/x/oauth2/jws)) = 0.5.0
Provides: bundled(golang(golang.org/x/oauth2/jwt)) = 0.5.0
Provides: bundled(golang(golang.org/x/sys/unix)) = 0.5.0
Provides: bundled(golang(google.golang.org/api/googleapi)) = 0.110.0
Provides: bundled(golang(google.golang.org/api/googleapi/transport)) = 0.110.0
Provides: bundled(golang(google.golang.org/api/iamcredentials/v1)) = 0.110.0
Provides: bundled(golang(google.golang.org/api/internal)) = 0.110.0
Provides: bundled(golang(google.golang.org/api/internal/gensupport)) = 0.110.0
Provides: bundled(golang(google.golang.org/api/internal/impersonate)) = 0.110.0
Provides: bundled(golang(google.golang.org/api/internal/third_party/uritemplates)) = 0.110.0
Provides: bundled(golang(google.golang.org/api/iterator)) = 0.110.0
Provides: bundled(golang(google.golang.org/api/option)) = 0.110.0
Provides: bundled(golang(google.golang.org/api/option/internaloption)) = 0.110.0
Provides: bundled(golang(google.golang.org/api/storage/v1)) = 0.110.0
Provides: bundled(golang(google.golang.org/api/transport)) = 0.110.0
Provides: bundled(golang(google.golang.org/api/transport/cert)) = 0.110.0
Provides: bundled(golang(google.golang.org/api/transport/grpc)) = 0.110.0
Provides: bundled(golang(google.golang.org/api/transport/http)) = 0.110.0
Provides: bundled(golang(google.golang.org/api/transport/http/internal/propagation)) = 0.110.0
Provides: bundled(golang(google.golang.org/api/transport/internal/dca)) = 0.110.0


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
* Mon May 29 2023 duyiwei <duyiwei@kylinos.cn> - 2.15.0-1
- upgrade version to 2.15.0

* Wed Jan 04 2023 liukuo <liukuo@kylinos.cn> - 2.14.0-2
- Fix %{_unitdir} not identified

* Fri May 27 2022 duyiwei <duyiwei@kylinos.cn> - 2.14.0-1
- update version to 2.14.0
- fix CVE-2022-1706

* Mon May 23 2022 duyiwei <duyiwei@kylinos.cn> - 2.13.0-1
- update version to 2.13.0

* Fri Dec 24 2021 duyiwei <duyiwei@kylinos.cn> - 2.9.0-1
- Package init
