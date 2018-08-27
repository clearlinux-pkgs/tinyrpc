#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tinyrpc
Version  : 0.9.3
Release  : 2
URL      : https://files.pythonhosted.org/packages/a6/0d/fc95d021561f1097361e16ebe06abf7acda74954eed88147ba7b3885ff49/tinyrpc-0.9.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/a6/0d/fc95d021561f1097361e16ebe06abf7acda74954eed88147ba7b3885ff49/tinyrpc-0.9.3.tar.gz
Summary  : A small, modular, transport and protocol neutral RPC library that, among other things, supports JSON-RPC and zmq.
Group    : Development/Tools
License  : MIT
Requires: tinyrpc-python3
Requires: tinyrpc-license
Requires: tinyrpc-python
Requires: gevent
Requires: pyzmq
Requires: requests
Requires: six
Requires: websocket_client
BuildRequires : buildreq-distutils3
BuildRequires : six

%description
============================================================

%package license
Summary: license components for the tinyrpc package.
Group: Default

%description license
license components for the tinyrpc package.


%package python
Summary: python components for the tinyrpc package.
Group: Default
Requires: tinyrpc-python3

%description python
python components for the tinyrpc package.


%package python3
Summary: python3 components for the tinyrpc package.
Group: Default
Requires: python3-core

%description python3
python3 components for the tinyrpc package.


%prep
%setup -q -n tinyrpc-0.9.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1535408201
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/tinyrpc
cp LICENSE %{buildroot}/usr/share/doc/tinyrpc/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/tinyrpc/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
