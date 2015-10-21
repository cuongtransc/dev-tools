angular.module('myapp')
    .controller('HomeController', ['$scope', 'SnapshotServices', function($scope, SnapshotServices) {
        $scope.listSnapshot = [];
        $scope.currentSnapshot = "";

        $scope.getSnapshots = function() {
            SnapshotServices.getSnapshots().then(function(data) {
                $scope.listSnapshot = data['snapshots'];
            });
        };

        $scope.backupDatabase = function() {
            SnapshotServices.backupDatabase($scope.getSnapshots).then(function(data) {
                if (data.status == "success") {} else {
                }
            });
        };

        $scope.restoreDatabase = function() {
            if ($scope.currentSnapshot) {
                SnapshotServices.restoreDatabase($scope.currentSnapshot).then(function(data) {
                    if (data.status == "success") {
                        $scope.currentSnapshot = "";
                    } else {

                    }
                });
            }
        };

        $scope.chooseSnapshot = function(snapshotId) {
            $scope.currentSnapshot = snapshotId;
//            console.log($scope.currentSnapshot)
        };
    }]);
