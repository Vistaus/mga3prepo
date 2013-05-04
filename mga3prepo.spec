Name:		mga3prepo
Version:	0.6
Release:	%mkrel 1
Summary:	A script to search packages in extra repositories
License:	GPL
Group:		System/Configuration/Packaging
Url:		http://glenbox.free.fr/%name/
Source0:	http://glenbox.free.fr/%name/%version/%name-%version.tar.gz

BuildArch:	noarch

BuildRequires:	gettext
BuildRequires:	python3-setuptools

Requires:	python3
Requires:	wget
Requires:	gzip
Requires:	xz

%description
A script in Python3 to search package from extra (unofficial or not) repositories.
Launch the script as 'mga3prepo' or with the name of the package as an argument.


%prep
%setup -q -n %name-%version

%build
%{__python3} i18n.py
%{__python3} ./setup.py build


%install
%{__python3} ./setup.py install -O1 --skip-build --root %{buildroot}
mkdir -p %{buildroot}%{_bindir}

install -D -m 755 %name \
	 %{buildroot}%{_bindir}/
	 
chmod +x %buildroot%{_bindir}/


### Install translations ###
pushd ./po
for f in *.po
do
		poname=${f:0:2}
		mkdir -p %buildroot%{_datadir}/locale/$poname/LC_MESSAGES
		install -m 644 usr/share/locale/$poname/LC_MESSAGES/%name.mo \
		"%{buildroot}%{_datadir}/locale/$poname/LC_MESSAGES/"
done
popd
#############################

%find_lang %name --with-html


%files -f %name.lang
%doc README COPYING
%{_bindir}/%{name}
%{python3_sitelib}/%name-%version-py%py3ver.egg-info



