'use strict';


// Declare app level module which depends on filters, and services
angular.module('myApp', ['myFilters']).
  config(['$routeProvider', function($routeProvider) {
    $routeProvider.when('/campaigns', {templateUrl: '/media/templates/campaign-list.html', controller: CampListCtrl});
    $routeProvider.when('/json/actual:campaignId', {templateUrl: '/media/templates/campaign-detail.html', controller: CampActualCtrl});
    $routeProvider.otherwise({redirectTo: '/campaigns'});
  }]);
  
