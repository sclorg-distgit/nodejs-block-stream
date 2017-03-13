%{?scl:%scl_package nodejs-block-stream}
%{!?scl:%global pkg_name %{name}}

%global enable_tests 0

%{?nodejs_find_provides_and_requires}

Name:       %{?scl_prefix}nodejs-block-stream
Version:    0.0.8
Release:    2%{?dist}
Summary:    A stream of blocks
License:    BSD
URL:        https://github.com/isaacs/block-stream
Source0:    http://registry.npmjs.org/block-stream/-/block-stream-%{version}.tgz
BuildArch:  noarch
ExclusiveArch: %{ix86} x86_64 %{arm} noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%if 0%{enable_tests}
BuildRequires:    %{?scl_prefix}npm(tap)
%endif

%description
Write data into it, and it'll output data in buffer blocks the size you
specify, padding with zeroes if necessary.

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/block-stream
cp -pr block-stream.js package.json %{buildroot}%{nodejs_sitelib}/block-stream

%nodejs_symlink_deps

%if 0%{enable_tests}
%check
%nodejs_symlink_deps --check
tap test/
%endif

%files
%{nodejs_sitelib}/block-stream
%doc README.md LICENCE

%changelog
* Mon Jan 16 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.0.8-2
- Clean up

* Wed Sep 07 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.0.8-1
- Updated with script

* Thu Oct 17 2013 Tomas Hrcka <thrcka@redhat.com> - 0.0.7-2
- replace provides and requires with macro

* Tue Jul 30 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.7-1
- new upstream release 0.0.7

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.6-7
- restrict to compatible arches

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.6-6
- add macro for EPEL6 dependency generation

* Fri Apr 12 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.0.6-6
- Add support for software collections

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 17 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.6-4
- correct Licensse tag
- include LICENCE file
- provide a better description

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.6-3
- add missing build section

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.6-2
- clean up for submission

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.6-1
- new upstream release 0.0.6

* Fri Apr 27 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.5-2
- guard Requires for F17 automatic depedency generation

* Sat Feb 25 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.5-1
- new upstream release 0.0.5

* Fri Jan 21 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.4-1
- initial package
