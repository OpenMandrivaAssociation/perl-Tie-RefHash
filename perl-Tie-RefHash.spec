
%define realname   Tie-RefHash
%define version    1.38
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Use references as hash keys
Source:     http://www.cpan.org/modules/by-module/Tie/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel


BuildArch: noarch

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
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes
%{_mandir}/man3/*
%perl_vendorlib/*


