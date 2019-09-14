#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : compat-libgit2-soname27
Version  : 0.27.8
Release  : 4
URL      : https://github.com/libgit2/libgit2/archive/v0.27.8.tar.gz
Source0  : https://github.com/libgit2/libgit2/archive/v0.27.8.tar.gz
Summary  : The git library, take 2
Group    : Development/Tools
License  : CC0-1.0 GPL-2.0 MIT
Requires: compat-libgit2-soname27-lib = %{version}-%{release}
Requires: compat-libgit2-soname27-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : glibc-dev
BuildRequires : libssh2-dev
BuildRequires : openssl-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(libcurl)
BuildRequires : python-dev
BuildRequires : python3
BuildRequires : python3-dev
BuildRequires : zlib-dev
# Suppress generation of debuginfo
%global debug_package %{nil}

%description
libgit2 - the Git linkable library
==================================
[![Azure Pipelines Build Status](https://dev.azure.com/libgit2/libgit2/_apis/build/status/libgit2)](https://dev.azure.com/libgit2/libgit2/_build/latest?definitionId=7)
[![Coverity Scan Build Status](https://scan.coverity.com/projects/639/badge.svg)](https://scan.coverity.com/projects/639)

%package lib
Summary: lib components for the compat-libgit2-soname27 package.
Group: Libraries
Requires: compat-libgit2-soname27-license = %{version}-%{release}

%description lib
lib components for the compat-libgit2-soname27 package.


%package license
Summary: license components for the compat-libgit2-soname27 package.
Group: Default

%description license
license components for the compat-libgit2-soname27 package.


%prep
%setup -q -n libgit2-0.27.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1567812760
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1567812760
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/compat-libgit2-soname27
cp COPYING %{buildroot}/usr/share/package-licenses/compat-libgit2-soname27/COPYING
cp deps/http-parser/LICENSE-MIT %{buildroot}/usr/share/package-licenses/compat-libgit2-soname27/deps_http-parser_LICENSE-MIT
cp examples/COPYING %{buildroot}/usr/share/package-licenses/compat-libgit2-soname27/examples_COPYING
pushd clr-build
%make_install
popd
## Remove excluded files
rm -f %{buildroot}/usr/include/git2.h
rm -f %{buildroot}/usr/include/git2/annotated_commit.h
rm -f %{buildroot}/usr/include/git2/attr.h
rm -f %{buildroot}/usr/include/git2/blame.h
rm -f %{buildroot}/usr/include/git2/blob.h
rm -f %{buildroot}/usr/include/git2/branch.h
rm -f %{buildroot}/usr/include/git2/buffer.h
rm -f %{buildroot}/usr/include/git2/checkout.h
rm -f %{buildroot}/usr/include/git2/cherrypick.h
rm -f %{buildroot}/usr/include/git2/clone.h
rm -f %{buildroot}/usr/include/git2/commit.h
rm -f %{buildroot}/usr/include/git2/common.h
rm -f %{buildroot}/usr/include/git2/config.h
rm -f %{buildroot}/usr/include/git2/cred_helpers.h
rm -f %{buildroot}/usr/include/git2/describe.h
rm -f %{buildroot}/usr/include/git2/diff.h
rm -f %{buildroot}/usr/include/git2/errors.h
rm -f %{buildroot}/usr/include/git2/filter.h
rm -f %{buildroot}/usr/include/git2/global.h
rm -f %{buildroot}/usr/include/git2/graph.h
rm -f %{buildroot}/usr/include/git2/ignore.h
rm -f %{buildroot}/usr/include/git2/index.h
rm -f %{buildroot}/usr/include/git2/indexer.h
rm -f %{buildroot}/usr/include/git2/inttypes.h
rm -f %{buildroot}/usr/include/git2/merge.h
rm -f %{buildroot}/usr/include/git2/message.h
rm -f %{buildroot}/usr/include/git2/net.h
rm -f %{buildroot}/usr/include/git2/notes.h
rm -f %{buildroot}/usr/include/git2/object.h
rm -f %{buildroot}/usr/include/git2/odb.h
rm -f %{buildroot}/usr/include/git2/odb_backend.h
rm -f %{buildroot}/usr/include/git2/oid.h
rm -f %{buildroot}/usr/include/git2/oidarray.h
rm -f %{buildroot}/usr/include/git2/pack.h
rm -f %{buildroot}/usr/include/git2/patch.h
rm -f %{buildroot}/usr/include/git2/pathspec.h
rm -f %{buildroot}/usr/include/git2/proxy.h
rm -f %{buildroot}/usr/include/git2/rebase.h
rm -f %{buildroot}/usr/include/git2/refdb.h
rm -f %{buildroot}/usr/include/git2/reflog.h
rm -f %{buildroot}/usr/include/git2/refs.h
rm -f %{buildroot}/usr/include/git2/refspec.h
rm -f %{buildroot}/usr/include/git2/remote.h
rm -f %{buildroot}/usr/include/git2/repository.h
rm -f %{buildroot}/usr/include/git2/reset.h
rm -f %{buildroot}/usr/include/git2/revert.h
rm -f %{buildroot}/usr/include/git2/revparse.h
rm -f %{buildroot}/usr/include/git2/revwalk.h
rm -f %{buildroot}/usr/include/git2/signature.h
rm -f %{buildroot}/usr/include/git2/stash.h
rm -f %{buildroot}/usr/include/git2/status.h
rm -f %{buildroot}/usr/include/git2/stdint.h
rm -f %{buildroot}/usr/include/git2/strarray.h
rm -f %{buildroot}/usr/include/git2/submodule.h
rm -f %{buildroot}/usr/include/git2/sys/commit.h
rm -f %{buildroot}/usr/include/git2/sys/config.h
rm -f %{buildroot}/usr/include/git2/sys/diff.h
rm -f %{buildroot}/usr/include/git2/sys/filter.h
rm -f %{buildroot}/usr/include/git2/sys/hashsig.h
rm -f %{buildroot}/usr/include/git2/sys/index.h
rm -f %{buildroot}/usr/include/git2/sys/mempack.h
rm -f %{buildroot}/usr/include/git2/sys/merge.h
rm -f %{buildroot}/usr/include/git2/sys/odb_backend.h
rm -f %{buildroot}/usr/include/git2/sys/openssl.h
rm -f %{buildroot}/usr/include/git2/sys/refdb_backend.h
rm -f %{buildroot}/usr/include/git2/sys/reflog.h
rm -f %{buildroot}/usr/include/git2/sys/refs.h
rm -f %{buildroot}/usr/include/git2/sys/repository.h
rm -f %{buildroot}/usr/include/git2/sys/stream.h
rm -f %{buildroot}/usr/include/git2/sys/time.h
rm -f %{buildroot}/usr/include/git2/sys/transport.h
rm -f %{buildroot}/usr/include/git2/tag.h
rm -f %{buildroot}/usr/include/git2/trace.h
rm -f %{buildroot}/usr/include/git2/transaction.h
rm -f %{buildroot}/usr/include/git2/transport.h
rm -f %{buildroot}/usr/include/git2/tree.h
rm -f %{buildroot}/usr/include/git2/types.h
rm -f %{buildroot}/usr/include/git2/version.h
rm -f %{buildroot}/usr/include/git2/worktree.h
rm -f %{buildroot}/usr/lib64/libgit2.so
rm -f %{buildroot}/usr/lib64/pkgconfig/libgit2.pc

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgit2.so.0.27.8
/usr/lib64/libgit2.so.27

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/compat-libgit2-soname27/COPYING
/usr/share/package-licenses/compat-libgit2-soname27/deps_http-parser_LICENSE-MIT
/usr/share/package-licenses/compat-libgit2-soname27/examples_COPYING
