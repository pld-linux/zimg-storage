# NOTE: zimg name reserved for https://github.com/sekrit-twc/zimg
# TODO:
# - system libevhtp, hiredis, ...
# - use (lib)onig
# - use plain lua where luajit not available (see system-lua for appropriate variables)
#
# Conditional build:
%bcond_without	apidocs		# do not build and package API docs
%bcond_without	static_libs	# don't build static libraries
#
Summary:	Light image storage and processing system
Summary(pl.UTF-8):	Lekki system do przechowywania i przetwarzania obrazów
Name:		zimg-storage
Version:	3.1.0
Release:	0.1
License:	BSD
Group:		Applications/Graphics
#Source0Download: https://github.com/buaazp/zimg/releases
Source0:	https://github.com/buaazp/zimg/archive/v%{version}/zimg-%{version}.tar.gz
# Source0-md5:	e2d003f9fe981ff7839a8a47b9a54dcc
Patch0:		zimg-system-lua.patch
URL:		http://zimg.buaa.us/
BuildRequires:	ImageMagick-devel
BuildRequires:	cmake >= 2.8
BuildRequires:	libevent-devel >= 2.0.20
BuildRequires:	libmemcached-devel >= 1.0.8
BuildRequires:	luajit-devel >= 2.0.4
BuildRequires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Project zimg is a light image storage and processing system. It's
written by C and it has high performance in image field. The zimg is
designed for high concurrency image server. It supports many features
for storing and processing images.  

%description -l pl.UTF-8
Projekt zimg to lekki system do przechowywania i przetwarzania
obrazów. Jest napisany w C ze zwróceniem uwagi na wysoką wydajność.
Jest przeznaczony dla serwera obrazów o dużym zrównolegleniu.
Obsługuje wiele opcji do przechowywania i przetwarzania obrazów.

%prep
%setup -q -n zimg-%{version}
%patch0 -p1

%build
install -d build
cd build
%cmake ../src
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install build/zimg $RPM_BUILD_ROOT%{_bindir}/zimg

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%attr(755,root,root) %{_bindir}/zimg
