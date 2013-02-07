%define		plugin		recaptcha
Summary:	DokuWiki reCAPTCHA Plugin
Summary(pl.UTF-8):	Wtyczka recaptcha dla DokuWiki
Name:		dokuwiki-plugin-%{plugin}
Version:	0.2
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	https://fosswiki.liip.ch/download/attachments/8224780/recaptcha_v0.2.tgz
# Source0-md5:	9fc3ae744ed2a0a81872b7d36798dfb1
URL:		http://www.dokuwiki.org/plugin:recaptcha
Requires:	dokuwiki >= 20061106
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}

%description
Lists all pages that link back to a given page using the first
headline as link title.

%prep
%setup -q -n %{plugin}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}
rm -f $RPM_BUILD_ROOT%{plugindir}/info.txt

%clean
rm -rf $RPM_BUILD_ROOT

%post
# force css cache refresh
if [ -f %{dokuconf}/local.php ]; then
	touch %{dokuconf}/local.php
fi

%files
%defattr(644,root,root,755)
%doc info.txt
%dir %{plugindir}
%{plugindir}/*.php
%dir %{plugindir}/conf
%{plugindir}/conf/*.php
%dir %{plugindir}/lang
%dir %{plugindir}/lang/en
%{plugindir}/lang/en/*.php
%dir %{plugindir}/lang/de
%{plugindir}/lang/de/*.php
%dir %{plugindir}/lib
%{plugindir}/lib/*.php
