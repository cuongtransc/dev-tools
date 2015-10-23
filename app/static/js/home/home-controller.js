angular.module('myapp')
    .controller('HomeController', ['$scope', '$timeout', 'SnapshotServices', function ($scope, $timeout, SnapshotServices) {
        $scope.listSnapshot = [];
        $scope.currentSnapshot = "";

        $scope.getSnapshots = function () {
            SnapshotServices.getSnapshots().then(function (data) {
                $scope.listSnapshot = data['snapshots'];
            });
        };

        $scope.backupDatabase = function () {
            $scope.showLoading();
            SnapshotServices.backupDatabase(function () {
                $timeout(function () {
                    $scope.hideLoading();
                }, 500);
                $scope.getSnapshots();
            }).then(function (data) {
                if (data.status == "success") {
                } else {
                }
            });
        };

        $scope.restoreDatabase = function () {
            if ($scope.currentSnapshot) {
                $scope.showLoading()
                SnapshotServices.restoreDatabase($scope.currentSnapshot, function () {
                    $timeout(function () {
                        $scope.hideLoading();
                    }, 500);
                }).then(function (data) {
                    if (data.status == "success") {
                        $scope.currentSnapshot = "";
                    } else {
                    }
                });
            }
        };

        $scope.chooseSnapshot = function (snapshotId, $event) {
            $('.active').removeClass('active');
            $($event.currentTarget).find('span').addClass('active');
            $scope.currentSnapshot = snapshotId;
//            console.log($scope.currentSnapshot)
        };
    }]);
