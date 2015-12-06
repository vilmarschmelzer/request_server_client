var requestapp = angular.module('requestapp',[]);

requestapp.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});

requestapp.controller('CategoryList', function ListCategory($scope, $log, $http){
    $scope.items = {}

    $scope.loadItems = function(){
        $scope.filter(1);
    };

    $scope.filter = function(page_number){

        var data = $.param({
                search: $scope.search,
                page:page_number});

            var config = {
                headers : {
                    'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8;'
                }
            }

        $http.post('/category-list-rest/', data,config)
        .success(function (data, status, headers, config) {
            $scope.page = data;
        })
        .error(function (data, status, header, config) {

        });
    };

    $scope.next = function(){

        page_number = $scope.page.number +1;
        if(page_number <= $scope.page.num_pages)
            $scope.filter(page_number);

    };

    $scope.previous = function(){

        page_number = $scope.page.number -1;
        if(page_number > 0)
            $scope.filter(page_number);
    };


});