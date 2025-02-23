%define upstream_name    Tie-RefHash

Name:		perl-%{upstream_name}
Version:	1.41
Release:	1

Summary:	Use references as hash keys
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Tie/%{upstream_name}-%{version}.tar.gz

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
%setup -q -n %{upstream_name}-%{version}
perl Makefile.PL INSTALLDIRS=vendor

%build
%make_build

%check
make test

%install
%make_install

%files
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*
