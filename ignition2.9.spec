# Generate devel rpm
%global with_devel 0
# Build project from bundled dependencies
%global with_bundled 1
# Build with debug info rpm
%global with_debug 1
# Run tests in check section
%global with_check 1
# Generate unit-test rpm
%global with_unit_test 1

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

%if ! 0%{?gobuild:1}
%define gobuild(o:) go build -ldflags "${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n')" -a -v -x %{?**};
%endif

# macros for Ignition
%global provider        github
%global provider_tld    com
%global project         coreos
%global repo            ignition
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}/v2
# define ldflags, buildflags, testflags here. The ldflags were
# taken from ./build. We will need to periodically check these
# for consistency
%global ldflags ' -X github.com/coreos/ignition/v2/internal/version.Raw=%{version} '
%global buildflags %nil
%global testflags %nil
%global dracutlibdir %{_prefix}/lib/dracut

Name:           ignition
Version:        2.9.0
Release:        1
Summary:        First boot installer and configuration tool
License:        ASL 2.0
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/v%{version}/%{repo}-%{version}.tar.gz
# Fix AWS probing by using the IMDS token URL to ensure that networking is up
# https://github.com/coreos/ignition/pull/1161
Patch0:         internal-providers-aws-probe-the-IMDS-token-URL.patch 

BuildRequires: golang >= 1.10

BuildRequires: libblkid-devel

# Requires for 'disks' stage
Recommends: btrfs-progs
Requires: dosfstools
Requires: gdisk
Requires: dracut
Requires: dracut-network

Obsoletes: ignition-dracut < 0.31.0-3

# Main rpm package BuildRequires
%if ! 0%{?with_bundled}
# Remaining dependencies not included in main packages (sorted)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/awserr)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/credentials)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/credentials/ec2rolecreds)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/ec2metadata)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/session)
BuildRequires: golang(github.com/aws/aws-sdk-go/service/s3)
BuildRequires: golang(github.com/aws/aws-sdk-go/service/s3/s3manager)
BuildRequires: golang(github.com/coreos/go-semver/semver)
BuildRequires: golang(github.com/coreos/go-systemd/dbus)
BuildRequires: golang(github.com/coreos/go-systemd/unit)
BuildRequires: golang(github.com/coreos/vcontext/json)
BuildRequires: golang(github.com/coreos/vcontext/path)
BuildRequires: golang(github.com/coreos/vcontext/report)
BuildRequires: golang(github.com/coreos/vcontext/tree)
BuildRequires: golang(github.com/coreos/vcontext/validate)
BuildRequires: golang(github.com/google/uuid)
BuildRequires: golang(github.com/pin/tftp)
BuildRequires: golang(github.com/vincent-petithory/dataurl)
BuildRequires: golang(github.com/vmware/vmw-guestinfo/rpcvmx)
BuildRequires: golang(github.com/vmware/vmw-guestinfo/vmcheck)
BuildRequires: golang(github.com/vmware/vmw-ovflib)
BuildRequires: golang(golang.org/x/net/http/httpproxy)
%endif

# Main package Provides (generated with go-mods-to-bundled-provides.py | sort)
%if 0%{?with_bundled}
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
Provides: bundled(golang(github.com/coreos/go-semver/semver)) = 0.3.0
Provides: bundled(golang(github.com/coreos/go-systemd/v22/dbus)) = 22.0.0
Provides: bundled(golang(github.com/coreos/go-systemd/v22/journal)) = 22.0.0
Provides: bundled(golang(github.com/coreos/go-systemd/v22/unit)) = 22.0.0
Provides: bundled(golang(github.com/coreos/vcontext/json)) = 0.0.0-20201120045928.gitb0e13dab675c
Provides: bundled(golang(github.com/coreos/vcontext/path)) = 0.0.0-20201120045928.gitb0e13dab675c
Provides: bundled(golang(github.com/coreos/vcontext/report)) = 0.0.0-20201120045928.gitb0e13dab675c
Provides: bundled(golang(github.com/coreos/vcontext/tree)) = 0.0.0-20201120045928.gitb0e13dab675c
Provides: bundled(golang(github.com/coreos/vcontext/validate)) = 0.0.0-20201120045928.gitb0e13dab675c
Provides: bundled(golang(github.com/google/renameio)) = 0.1.0
Provides: bundled(golang(github.com/google/uuid)) = 1.1.1
Provides: bundled(golang(github.com/pin/tftp)) = 2.1.0
Provides: bundled(golang(github.com/pin/tftp/netascii)) = 2.1.0
Provides: bundled(golang(github.com/stretchr/testify/assert)) = 1.5.1
Provides: bundled(golang(github.com/vincent-petithory/dataurl)) = 0.0.0-20160330182126.git9a301d65acbb
Provides: bundled(golang(github.com/vmware/vmw-guestinfo/bdoor)) = 0.0.0-20170707015358.git25eff159a728
Provides: bundled(golang(github.com/vmware/vmw-guestinfo/message)) = 0.0.0-20170707015358.git25eff159a728
Provides: bundled(golang(github.com/vmware/vmw-guestinfo/rpcout)) = 0.0.0-20170707015358.git25eff159a728
Provides: bundled(golang(github.com/vmware/vmw-guestinfo/rpcvmx)) = 0.0.0-20170707015358.git25eff159a728
Provides: bundled(golang(github.com/vmware/vmw-guestinfo/vmcheck)) = 0.0.0-20170707015358.git25eff159a728
Provides: bundled(golang(github.com/vmware/vmw-ovflib)) = 0.0.0-20170608004843.git1f217b9dc714
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
%endif


%description
Ignition is a utility used to manipulate systems during the initramfs.
This includes partitioning disks, formatting partitions, writing files
(regular files, systemd units, etc.), and configuring users. On first
boot, Ignition reads its configuration from a source of truth (remote
URL, network metadata service, hypervisor bridge, etc.) and applies
the configuration.

############## devel subpackage ##############

%if 0%{?with_devel}
%package devel
Summary:       %{summary}
BuildArch:     noarch
License:       ASL 2.0

# devel subpackage BuildRequires
%if 0%{?with_check} && ! 0%{?with_bundled}
# These buildrequires are only for our tests (check) (sorted)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/awserr)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/credentials)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/credentials/ec2rolecreds)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/ec2metadata)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/session)
BuildRequires: golang(github.com/aws/aws-sdk-go/service/s3)
BuildRequires: golang(github.com/aws/aws-sdk-go/service/s3/s3manager)
BuildRequires: golang(github.com/coreos/go-semver/semver)
BuildRequires: golang(github.com/coreos/go-systemd/dbus)
BuildRequires: golang(github.com/coreos/go-systemd/unit)
BuildRequires: golang(github.com/coreos/vcontext/json)
BuildRequires: golang(github.com/coreos/vcontext/path)
BuildRequires: golang(github.com/coreos/vcontext/report)
BuildRequires: golang(github.com/coreos/vcontext/tree)
BuildRequires: golang(github.com/coreos/vcontext/validate)
BuildRequires: golang(github.com/google/uuid)
BuildRequires: golang(github.com/pin/tftp)
BuildRequires: golang(github.com/vincent-petithory/dataurl)
BuildRequires: golang(github.com/vmware/vmw-guestinfo/rpcvmx)
BuildRequires: golang(github.com/vmware/vmw-guestinfo/vmcheck)
BuildRequires: golang(github.com/vmware/vmw-ovflib)
BuildRequires: golang(golang.org/x/net/http/httpproxy)
%endif

# devel subpackage Requires. This is basically the source code from
# all of the libraries that ignition imports during build. (sorted)
Requires:      golang(github.com/aws/aws-sdk-go/aws)
Requires:      golang(github.com/aws/aws-sdk-go/aws/awserr)
Requires:      golang(github.com/aws/aws-sdk-go/aws/credentials)
Requires:      golang(github.com/aws/aws-sdk-go/aws/credentials/ec2rolecreds)
Requires:      golang(github.com/aws/aws-sdk-go/aws/ec2metadata)
Requires:      golang(github.com/aws/aws-sdk-go/aws/session)
Requires:      golang(github.com/aws/aws-sdk-go/service/s3)
Requires:      golang(github.com/aws/aws-sdk-go/service/s3/s3manager)
Requires:      golang(github.com/coreos/go-semver/semver)
Requires:      golang(github.com/coreos/go-systemd/dbus)
Requires:      golang(github.com/coreos/go-systemd/unit)
Requires:      golang(github.com/coreos/vcontext/json)
Requires:      golang(github.com/coreos/vcontext/path)
Requires:      golang(github.com/coreos/vcontext/report)
Requires:      golang(github.com/coreos/vcontext/tree)
Requires:      golang(github.com/coreos/vcontext/validate)
Requires:      golang(github.com/google/uuid)
Requires:      golang(github.com/pin/tftp)
Requires:      golang(github.com/vincent-petithory/dataurl)
Requires:      golang(github.com/vmware/vmw-guestinfo/rpcvmx)
Requires:      golang(github.com/vmware/vmw-guestinfo/vmcheck)
Requires:      golang(github.com/vmware/vmw-ovflib)
Requires:      golang(golang.org/x/net/http/httpproxy)

# devel subpackage Provides (sorted)
Provides:      golang(%{import_path}/config) = %{version}-%{release}
Provides:      golang(%{import_path}/config/merge) = %{version}-%{release}
Provides:      golang(%{import_path}/config/shared) = %{version}-%{release}
Provides:      golang(%{import_path}/config/shared/errors) = %{version}-%{release}
Provides:      golang(%{import_path}/config/shared/validations) = %{version}-%{release}
Provides:      golang(%{import_path}/config/translate) = %{version}-%{release}
Provides:      golang(%{import_path}/config/translate/tests/pkga) = %{version}-%{release}
Provides:      golang(%{import_path}/config/translate/tests/pkgb) = %{version}-%{release}
Provides:      golang(%{import_path}/config/util) = %{version}-%{release}
Provides:      golang(%{import_path}/config/v3_0) = %{version}-%{release}
Provides:      golang(%{import_path}/config/v3_0/types) = %{version}-%{release}
Provides:      golang(%{import_path}/config/v3_1_experimental) = %{version}-%{release}
Provides:      golang(%{import_path}/config/v3_1_experimental/translate) = %{version}-%{release}
Provides:      golang(%{import_path}/config/v3_1_experimental/types) = %{version}-%{release}
Provides:      golang(%{import_path}/config/validate) = %{version}-%{release}
Provides:      golang(%{import_path}/tests) = %{version}-%{release}
Provides:      golang(%{import_path}/tests/negative/files) = %{version}-%{release}
Provides:      golang(%{import_path}/tests/negative/filesystems) = %{version}-%{release}
Provides:      golang(%{import_path}/tests/negative/general) = %{version}-%{release}
Provides:      golang(%{import_path}/tests/negative/partitions) = %{version}-%{release}
Provides:      golang(%{import_path}/tests/negative/proxy) = %{version}-%{release}
Provides:      golang(%{import_path}/tests/negative/regression) = %{version}-%{release}
Provides:      golang(%{import_path}/tests/negative/security) = %{version}-%{release}
Provides:      golang(%{import_path}/tests/negative/timeouts) = %{version}-%{release}
Provides:      golang(%{import_path}/tests/positive/files) = %{version}-%{release}
Provides:      golang(%{import_path}/tests/positive/filesystems) = %{version}-%{release}
Provides:      golang(%{import_path}/tests/positive/general) = %{version}-%{release}
Provides:      golang(%{import_path}/tests/positive/partitions) = %{version}-%{release}
Provides:      golang(%{import_path}/tests/positive/passwd) = %{version}-%{release}
Provides:      golang(%{import_path}/tests/positive/proxy) = %{version}-%{release}
Provides:      golang(%{import_path}/tests/positive/regression) = %{version}-%{release}
Provides:      golang(%{import_path}/tests/positive/security) = %{version}-%{release}
Provides:      golang(%{import_path}/tests/positive/systemd) = %{version}-%{release}
Provides:      golang(%{import_path}/tests/positive/timeouts) = %{version}-%{release}
Provides:      golang(%{import_path}/tests/register) = %{version}-%{release}
Provides:      golang(%{import_path}/tests/registry) = %{version}-%{release}
Provides:      golang(%{import_path}/tests/servers) = %{version}-%{release}
Provides:      golang(%{import_path}/tests/types) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.
%endif

############## unit-test-devel subpackage ##############
%if 0%{?with_unit_test} && 0%{?with_devel}
%package unit-test-devel
Summary:         Unit tests for %{name} package
License:         ASL 2.0
%if 0%{?with_check}
#Here comes all BuildRequires: PACKAGE the unit tests
#in %%check section need for running
%endif

# test subpackage tests code from devel subpackage
Requires:        %{name}-devel = %{version}-%{release}

%if 0%{?with_check} && ! 0%{?with_bundled}
BuildRequires: golang(github.com/stretchr/testify/assert)
%endif

Requires:      golang(github.com/stretchr/testify/assert)

%description unit-test-devel
%{summary}

This package contains unit tests for project
providing packages with %{import_path} prefix.
%endif


############## validate subpackage ##############
%package validate

Summary:  Validation tool for Ignition configs
License:  ASL 2.0

Conflicts: ignition < 0.31.0-3

%description validate
Ignition is a utility used to manipulate systems during the initramfs.
This includes partitioning disks, formatting partitions, writing files
(regular files, systemd units, etc.), and configuring users. On first
boot, Ignition reads its configuration from a source of truth (remote
URL, network metadata service, hypervisor bridge, etc.) and applies
the configuration.

This package contains a tool for validating Ignition configurations.

############## validate-nonlinux subpackage ##############
%package validate-nonlinux

Summary:   Validation tool for Ignition configs for macOS and Windows
License:   ASL 2.0
BuildArch: noarch

Conflicts: ignition < 0.31.0-3

%description validate-nonlinux
This package contains macOS and Windows ignition-validate binaries built
through cross-compilation. Do not install it. It is only used for
building binaries to sign by Fedora release engineering and include on the
Ignition project's Github releases page.

%prep
%autosetup -p1

%build
# Set up PWD as a proper import path for go
mkdir -p src/%{provider}.%{provider_tld}/%{project}
ln -s ../../../ src/%{provider_prefix}

export LDFLAGS=%{ldflags}
# Enable SELinux relabeling
export LDFLAGS+=' -X github.com/coreos/ignition/v2/internal/distro.selinuxRelabel=true '

# Modules
export GO111MODULE=on
export GOFLAGS='-mod=vendor'

echo "Building ignition..."
%gobuild -o ./ignition %{import_path}/internal

echo "Building ignition-validate..."
%gobuild -o ./ignition-validate %{import_path}/validate

echo "Building macOS ignition-validate"
export GOARCH=amd64
export GOOS=darwin
%gobuild -o ./ignition-validate-x86_64-apple-darwin %{import_path}/validate

echo "Building Windows ignition-validate"
export GOARCH=amd64
export GOOS=windows
%gobuild -o ./ignition-validate-x86_64-pc-windows-gnu.exe %{import_path}/validate

# Set this back, just in case
export GOARCH=
export GOOS=linux

%install
# dracut modules
install -d -p %{buildroot}/%{dracutlibdir}/modules.d
install -d -p %{buildroot}/%{_prefix}/lib/systemd/system
cp -r dracut/* %{buildroot}/%{dracutlibdir}/modules.d/
install -m 0644 -t %{buildroot}/%{_prefix}/lib/systemd/system/ systemd/*

# ignition
install -d -p %{buildroot}%{_bindir}
install -p -m 0755 ./ignition-validate %{buildroot}%{_bindir}

install -d -p %{buildroot}%{_datadir}/ignition
install -p -m 0644 ./ignition-validate-x86_64-apple-darwin %{buildroot}%{_datadir}/ignition
install -p -m 0644 ./ignition-validate-x86_64-pc-windows-gnu.exe %{buildroot}%{_datadir}/ignition

# The ignition binary is only for dracut, and is dangerous to run from
# the command line.  Install directly into the dracut module dir.
install -p -m 0755 ./ignition %{buildroot}/%{dracutlibdir}/modules.d/30ignition

# source codes for building projects
%if 0%{?with_devel}
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
echo "%%dir %%{gopath}/src/%%{import_path}/." >> devel.file-list
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . \( -iname "*.go" -or -iname "*.s" \) \! -iname "*_test.go" | grep -v "vendor") ; do
    dirprefix=$(dirname $file)
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$dirprefix
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> devel.file-list

    while [ "$dirprefix" != "." ]; do
        echo "%%dir %%{gopath}/src/%%{import_path}/$dirprefix" >> devel.file-list
        dirprefix=$(dirname $dirprefix)
    done
done
%endif

# testing files for this project
%if 0%{?with_unit_test} && 0%{?with_devel}
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
# find all *_test.go files and generate unit-test-devel.file-list
for file in $(find . -iname "*_test.go" | grep -v "vendor") ; do
    dirprefix=$(dirname $file)
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$dirprefix
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> unit-test-devel.file-list

    while [ "$dirprefix" != "." ]; do
        echo "%%dir %%{gopath}/src/%%{import_path}/$dirprefix" >> devel.file-list
        dirprefix=$(dirname $dirprefix)
    done
done
%endif

%if 0%{?with_devel}
sort -u -o devel.file-list devel.file-list
%endif

%check
%if 0%{?with_check} && 0%{?with_unit_test} && 0%{?with_devel}
%if ! 0%{?with_bundled}
export GOPATH=%{buildroot}/%{gopath}:%{gopath}
%else
# Since we aren't packaging up the vendor directory we need to link
# back to it somehow. Hack it up so that we can add the vendor
# directory from BUILD dir as a gopath to be searched when executing
# tests from the BUILDROOT dir.
ln -s ./ ./vendor/src # ./vendor/src -> ./vendor

export GOPATH=%{buildroot}/%{gopath}:$(pwd)/vendor:%{gopath}
%endif

%if ! 0%{?gotest:1}
%global gotest go test
%endif

%gotest %{import_path}/config
%gotest %{import_path}/config/merge
%gotest %{import_path}/config/translate
%gotest %{import_path}/config/v3_0
%gotest %{import_path}/config/v3_0/types
%gotest %{import_path}/config/v3_1
%gotest %{import_path}/config/v3_1/types
%gotest %{import_path}/config/v3_2
%gotest %{import_path}/config/v3_2/types
%gotest %{import_path}/config/validate
%gotest %{import_path}/internal/exec/stages/files
%gotest %{import_path}/internal/exec/util
%gotest %{import_path}/internal/registry
%gotest %{import_path}/internal/util
%gotest %{import_path}/tests
%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files
%license LICENSE
%doc README.md docs/
%{dracutlibdir}/modules.d/*
%{_prefix}/lib/systemd/system/*.service

%files validate
%doc README.md
%license LICENSE
%{_bindir}/%{name}-validate

%files validate-nonlinux
%license LICENSE
%dir %{_datadir}/ignition
%{_datadir}/ignition/ignition-validate-x86_64-apple-darwin
%{_datadir}/ignition/ignition-validate-x86_64-pc-windows-gnu.exe

%if 0%{?with_devel}
%files devel -f devel.file-list
%license LICENSE
%doc README.md code-of-conduct.md CONTRIBUTING.md
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%files unit-test-devel -f unit-test-devel.file-list
%license LICENSE
%doc README.md code-of-conduct.md CONTRIBUTING.md
%endif

%changelog
* Fri Dec 24 2021 duyiwei <duyiwei@kylinos.cn> - 2.9.0-1
- Package init
