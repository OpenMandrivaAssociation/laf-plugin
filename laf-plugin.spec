
#TODO: provide javadoc after/if upstream fixes the win specific build

Name:           laf-plugin
Version:        1.0
Release:        %mkrel 0.0.3
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
%remove_java_binaries

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
  
