# Run optional test
%bcond_without perl_Math_BigInt_enables_optional_test

Name:           perl-Math-BigInt
Epoch:          1
%global cpan_version 1.999811
# Keep 4-digit version to compete with perl.spec
Version:        %(echo %{cpan_version} | sed 's/\(\.....\)/\1./')
Release:        7%{?dist}
Summary:        Arbitrary-size integer and float mathematics
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Math-BigInt/
Source0:        http://www.cpan.org/authors/id/P/PJ/PJACKLAM/Math-BigInt-%{cpan_version}.tar.gz
# Document Math::BigInt::CalcEmu requires Math::BigInt, bug #1689914,
# CPAN RT#85015, fixes in 1.999815 upstream by removing the module
Patch0:         Math-BigInt-1.999811-Document-Math-BigInt-CalcEmu-requires-Math-BigInt.patch
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
# File::Spec not used on recent perl
BuildRequires:  perl(integer)
BuildRequires:  perl(Math::Complex) >= 1.39
BuildRequires:  perl(overload)
# Tests:
BuildRequires:  perl(base)
BuildRequires:  perl(Config)
# Config::Tiny not used
BuildRequires:  perl(lib)
# Module::Signature not used
# Scalar::Util not used
# Socket not used
BuildRequires:  perl(Test::More) >= 0.94
%if %{with perl_Math_BigInt_enables_optional_test}
# Optional tests:
# This core module must be buildable without non-core modules at bootstrap.
%if !%{defined perl_bootstrap}
BuildRequires:  perl(Test::Pod) >= 1.22
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
BuildRequires:  perl(Pod::Coverage) >= 0.18
%endif
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Math::Complex) >= 1.39
Conflicts:      perl < 4:5.22.0-347

# Do not export unversioned module
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Math::BigInt\\)\\s*$

%description
This provides Perl modules for arbitrary-size integer and float mathematics.

%prep
%setup -q -n Math-BigInt-%{cpan_version}
%patch0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
# NEW file is useless
%doc BUGS CHANGES CREDITS examples GOALS HISTORY README TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Apr 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.9998.11-7
- Enable gating 

* Mon Mar 18 2019 Petr Pisar <ppisar@redhat.com> - 1:1.9998.11-6
- Document Math::BigInt::CalcEmu requires Math::BigInt (bug #1689914)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.9998.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.9998.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.9998.11-3
- Perl 5.26 re-rebuild of bootstrapped packages

* Sat Jun 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.9998.11-2
- Perl 5.26 rebuild

* Fri Mar 17 2017 Petr Pisar <ppisar@redhat.com> - 1.9998.11-1
- 1.999811 bump

* Thu Mar 02 2017 Petr Pisar <ppisar@redhat.com> - 1.9998.10-1
- 1.999810 bump

* Mon Feb 13 2017 Petr Pisar <ppisar@redhat.com> - 1.9998.09-1
- 1.999809 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9998.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Paul Howarth <paul@city-fan.org> - 1.9998.08-1
- 1.999808 bump

* Mon Jan 02 2017 Petr Pisar <ppisar@redhat.com> - 1.9998.07-1
- 1.999807 bump

* Wed Dec 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.9998.06-1
- 1.999806 bump

* Mon Dec 12 2016 Petr Pisar <ppisar@redhat.com> - 1.9998.05-1
- 1.999805 bump

* Fri Dec 09 2016 Petr Pisar <ppisar@redhat.com> - 1.9998.04-1
- 1.999804 bump

* Mon Dec 05 2016 Petr Pisar <ppisar@redhat.com> - 1.9998.03-1
- 1.999803 bump

* Thu Dec 01 2016 Petr Pisar <ppisar@redhat.com> - 1.9998.02-1
- 1.999802 bump

* Fri Nov 25 2016 Petr Pisar <ppisar@redhat.com> - 1.9998.01-1
- 1.999801 bump

* Fri Nov 18 2016 Petr Pisar <ppisar@redhat.com> - 1.9998.00-1
- 1.999800 bump

* Tue Nov 08 2016 Petr Pisar <ppisar@redhat.com> - 1.9997.27-1
- 1.999727 bump

* Mon Jul 18 2016 Petr Pisar <ppisar@redhat.com> - 1.9997.26-1
- 1.999726 bump

* Mon Jun 20 2016 Petr Pisar <ppisar@redhat.com> - 1.9997.24-1
- 1.999724 bump

* Wed Jun 15 2016 Petr Pisar <ppisar@redhat.com> - 1.9997.23-1
- 1.999723 bump

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.9997.22-3
- Perl 5.24 re-rebuild of bootstrapped packages

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.9997.22-2
- Perl 5.24 rebuild

* Wed Apr 27 2016 Petr Pisar <ppisar@redhat.com> - 1.9997.22-1
- 1.999722 bump

* Tue Apr 26 2016 Petr Pisar <ppisar@redhat.com> - 1.9997.20-1
- 1.999720 bump

* Mon Apr 18 2016 Petr Pisar <ppisar@redhat.com> - 1.9997.17-1
- 1.999717 bump

* Tue Apr 05 2016 Petr Pisar <ppisar@redhat.com> - 1.9997.16-1
- 1.999716 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9997.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 06 2016 Petr Pisar <ppisar@redhat.com> - 1.9997.15-1
- 1.999715 bump

* Mon Jan 04 2016 Petr Pisar <ppisar@redhat.com> - 1.9997.14-1
- 1.999714 bump

* Mon Nov 16 2015 Petr Pisar <ppisar@redhat.com> - 1.9997.10-1
- 1.999710 bump

* Tue Nov 10 2015 Petr Pisar <ppisar@redhat.com> - 1.9997.09-1
- 1.999709 bump

* Thu Nov 05 2015 Petr Pisar <ppisar@redhat.com> - 1.9997.08-1
- 1.999708 bump

* Mon Nov 02 2015 Petr Pisar <ppisar@redhat.com> 1.9997.07-354
- Specfile autogenerated by cpanspec 1.78.
- Use bundled modules when bootstrapping
