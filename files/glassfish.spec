Name            : glassfish
Version         : 3.0.1
Release         : 2
Summary         : Java application server
Group           : System Environment/Daemons

Source0         : http://download.java.net/%{name}/%{version}/release/%{name}-%{version}.zip
Source1         : %{name}.init
URL             : https://glassfish.dev.java.net/
Vendor          : Sun Microsystems
License         : CDDL
Packager        : Dan Carley <dan.carley@gmail.com>

BuildArch       : noarch
BuildRoot       : %{_tmppath}/%{name}-%{version}-root
BuildRequires   : unzip
Requires        : java >= 1:1.6.0
Requires(pre)   : shadow-utils

%description
Open source Java application server developed by Sun/Oracle.

%prep
%setup -q -n %{name}v3

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}/opt/%{name}
cp -R . %{buildroot}/opt/%{name}
install -d -m 755 %{buildroot}%{_initrddir}
install -p -m 755 %{SOURCE1} %{buildroot}%{_initrddir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%dir %{_initrddir}/%{name}
%dir /opt/%{name}
/opt/%{name}/.org.opensolaris,pkg
/opt/%{name}/bin
/opt/%{name}/mq
/opt/%{name}/javadb
/opt/%{name}/pkg
%dir /opt/%{name}/glassfish
/opt/%{name}/glassfish/bin
/opt/%{name}/glassfish/modules
/opt/%{name}/glassfish/lib
/opt/%{name}/glassfish/docs
/opt/%{name}/glassfish/config
/opt/%{name}/glassfish/osgi
/opt/%{name}/glassfish/legal
%attr(-,%{name},%{name}) /opt/%{name}/glassfish/domains

%pre
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || \
    useradd -r -g %{name} -d /opt/${name} -s /sbin/nologin -c "Glassfish Daemon" %{name}
exit 0

%changelog
* Fri Nov 26 2010 Dan Carley <dan.carley@gmail.com> 3.0.1-2
- Improved RC script.
- Remove dupe file listing warnings.
- Only supports the single default domain for now.

* Thu Oct 28 2010 Dan Carley <dan.carley@gmail.com> 3.0.1-1
- Initial package created from binary GlassFish release.
