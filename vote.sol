// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Voting {
    address public admin;
    mapping(uint256 => uint256) public votes;

    event Voted(uint256 candidateId);

    constructor() {
        admin = msg.sender;
    }

    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can perform this operation");
        _;
    }

    function vote(uint256 candidateId) external {
        require(candidateId > 0 && candidateId <= 5, "Invalid candidate ID");
        votes[candidateId]++;
        emit Voted(candidateId);
    }

    function getVotes(uint256 candidateId) external view returns (uint256) {
        require(candidateId > 0 && candidateId <= 5, "Invalid candidate ID");
        return votes[candidateId];
    }
}
