#!/usr/bin/perl -w -I/usr/sbin
use strict;
use DBI;
use CGI qw/:standard *table/;
use CGI::Carp qw(fatalsToBrowser);
use LWP::Simple qw(!head);
use LWP::UserAgent;
use HTTP::Request::Common qw(POST);

#debug
#open (OUTFILE, "> google_weather_debug.txt");


my $userAgent = LWP::UserAgent->new(agent => 'perl post');
my $post_code=param("postcode");

if ($post_code=~/^([\(\)\w\d\-\s]+)$/){
    $post_code=$1;
}else{
   die "Postcode may contain invalid characters: $!";
}



my $url="http://www.google.com/ig/api?weather=$post_code";


#sends the request xml off to the url
my $response = $userAgent->get($url);


unless($response->is_success){
	
    print OUTFILE $response->error_as_HTML;
	
}

#gets result (i.e. xml returned from post)
my $result=$response->content;
  
$result =~ /(<current_conditions>.*?<\/current_conditions>)/; 
my $current_conditions=$1; 
#debug
print OUTFILE "$current_conditions\n";
    
    print "Content-Type: text/xml\n\n";

    print qq($current_conditions);    
    

