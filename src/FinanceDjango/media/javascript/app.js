'use strict';


// Declare app level module which depends on filters, and services
angular.module('myApp', ['ui','myFilters']).
  config(['$routeProvider', function($routeProvider) {
    $routeProvider.when('/campaigns', {templateUrl: '/media/templates/campaign-list.html', controller: CampListCtrl});
    $routeProvider.when('/campaigns/:campaignId', {templateUrl: '/media/templates/campaign-detail.html', controller: CampActualCtrl});
    $routeProvider.when('/create', {templateUrl: '/media/templates/create-campaign.html', controller: CreateCampCtrl});
    $routeProvider.when('/types');
    $routeProvider.when('/products');    
    $routeProvider.when('/channels');    
    $routeProvider.when('/reps');
    $routeProvider.when('/CPs');    
   
    $routeProvider.otherwise({redirectTo: '/campaigns'});
  }]);
  
