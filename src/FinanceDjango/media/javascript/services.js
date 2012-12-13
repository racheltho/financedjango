'use strict';

/* Services */
angular.module('myAppServices', ['ngResource']).
    factory('Campaign', function($resource){
  return $resource('json/actual:campaignId.json', {}, {
    query: {method:'GET', params:{campaignId:'campaigns'}, isArray:true}
  });
});


// Demonstrate how to register services
// In this case it is a simple value service.
angular.module('myApp.services', []).
  value('version', '0.1');