Summary:	Full-stack platform-specific package for GitLab CE
Name:		omnibus-gitlab
Version:	8.11.2
Release:	0.1
License:	MIT
Group:		Applications/WWW
URL:		https://gitlab.com/gitlab-org/omnibus-gitlab/
Requires:	docker-registry >= 2
Requires:	gitlab-ce = %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GitLab Community Edition (CE) is open source software to collaborate
on code. Create projects and repositories, manage access and do code
reviews. GitLab CE is on-premises software that you can install and
use on your server(s).

This package contains dependencies that resembles gitlab-omnibus
packaging.

%prep
%setup -qcT

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
