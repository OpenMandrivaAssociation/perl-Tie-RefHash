%define upstream_name    Tie-RefHash
%define upstream_version 1.39

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Use references as hash keys
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Tie/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module provides the ability to use references as hash keys if you
first 'tie' the hash variable to this module. Normally, only the keys of
the tied hash itself are preserved as references; to use references as keys
in hashes-of-hashes, use Tie::RefHash::Nestable, included as part of
Tie::RefHash.

It is implemented using the standard perl TIEHASH interface. Please see the
'tie' entry in perlfunc(1) and perltie(1) for more information.

The Nestable version works by looking for hash references being stored and
converting them to tied hashes so that they too can have references as
keys. This will happen without warning whenever you store a reference to
one of your own hashes in the tied hash.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 1.390.0-2mdv2011.0
+ Revision: 657474
- rebuild for updated spec-helper

* Sun Mar 06 2011 Sandro Cazzaniga <kharec@mandriva.org> 1.390.0-1
+ Revision: 642388
- New version

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 1.380.0-1mdv2010.0
+ Revision: 401503
- rebuild using %%perl_convert_version
- fixed license field

* Mon May 11 2009 Jérôme Quelin <jquelin@mandriva.org> 1.38-1mdv2010.0
+ Revision: 374297
- import perl-Tie-RefHash


* Mon May 11 2009 cpan2dist 1.38-1mdv
- initial mdv release, generated with cpan2dist

