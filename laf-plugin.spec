
#TODO: provide javadoc after/if upstream fixes the win specific build

Name:           laf-plugin
Version:        1.0
Release:        1
Summary:        Generic plugin framework for Java look-and-feels
License:        BSD
Group:          Development/Java
Url:            https://laf-plugin.dev.java.net/
Source0:        https://laf-plugin.dev.java.net/files/documents/4261/50297/laf-plugin-all.zip
Source1:        build.xml
BuildRequires:  jpackage-utils
BuildRequires:  java-rpmbuild 
BuildRequires:  ant
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The goal of this project is to provide a generic plugin framework for 
look-and-feels and define the interface of a common kind of plugins - 
the component plugins.

#%package        javadoc
#Summary:        Javadoc for %{name}
#Group:          Development/Java
#
#%description javadoc
#Javadoc for %{name}.

%prep
%setup -q -c %{name}-%{version}
cp %{SOURCE1} build.xml
rm -rf drop/*

%build
#ln -s $(build-classpath asm2/asm2) lib/asm-all-2.2.2.jar
%{ant} all

%install
rm -rf %{buildroot}
install -m644 drop/%{name}-50.jar -D %{buildroot}%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

#install -d %{buildroot}%{_javadocdir}/%{name}-%{version}
#cp -r docs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
#ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar

#%files javadoc
#%defattr(644,root,root,755)
#%{_javadocdir}/%{name}
#%{_javadocdir}/%{name}-%{version}
  


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0-0.0.4mdv2011.0
+ Revision: 620046
- the mass rebuild of 2010.0 packages

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 1.0-0.0.3mdv2010.0
+ Revision: 436083
- rebuild

* Mon Feb 25 2008 Alexander Kurtakov <akurtakov@mandriva.org> 1.0-0.0.2mdv2008.1
+ Revision: 174701
- wrap description

* Mon Feb 25 2008 Alexander Kurtakov <akurtakov@mandriva.org> 1.0-0.0.1mdv2008.1
+ Revision: 174543
- import laf-plugin


