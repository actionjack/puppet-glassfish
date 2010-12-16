Name            : glassfish
Version         : 3.0.1
Release         : 3
Summary         : Java application server
Group           : System Environment/Daemons
Source0         : http://download.java.net/%{name}/%{version}/release/%{name}-%{version}.zip
Source1         : %{name}.init
URL             : https://glassfish.dev.java.net/
Vendor          : Sun Microsystems
License         : CDDL
Packager        : Martin Jackson <martin@uncommonsense-uk.com>
BuildArch       : noarch
BuildRoot       : %{_tmppath}/%{name}-%{version}-root
BuildRequires   : unzip
Requires        : java >= 1:1.6.0
Requires(pre)   : shadow-utils

%description
Open source Java application server developed by Sun/Oracle.

%prep
%setup -q -n %{name}v3

# Change relative path to absolute for AS_INSTALL
sed -i -e "s/^AS_INSTALL=.*/AS_INSTALL=\/opt\/glassfish\/glassfish/1" glassfish/bin/asadmin
sed -i -e "s/^AS_INSTALL=.*/AS_INSTALL=\/opt\/glassfish\/glassfish/1" bin/asadmin

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

%post
ln -s /opt/glassfish/bin/asadmin /usr/bin/asadmin
ln -s /opt/glassfish/bin/pkg /usr/bin/pkg
ln -s /opt/glassfish/bin/updatetool /usr/bin/updatetool
touch /opt/glassfish/.aspass

%changelog
* Thu Dec 12 2010 Martin Jackson <martin@uncommonsense-uk.com> 3.0.1-3
- Changed relative path name of AS_INSTALL variable to absolute
- Created soft links of all executiable files in /opt/glassfish/bin to /usr/bin
- Locked init script to domain1 start up only in prep for multi domains
- Created empty asadamin password place holder file

* Fri Nov 26 2010 Dan Carley <dan.carley@gmail.com> 3.0.1-2
- Improved RC script.
- Remove dupe file listing warnings.
- Only supports the single default domain for now.

* Thu Oct 28 2010 Dan Carley <dan.carley@gmail.com> 3.0.1-1
- Initial package created from binary GlassFish release.
