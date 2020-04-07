export default data = [
    {
        id: 'TownCenter',
        description: 'You are in the town center',
        choices: [
            {
                id: 1,
                description: 'Go to bar',
                res_node: 'Bar'
            },
            {
                id: 2,
                description: 'Go to townhall',
                res_node: 'TownHall'
            },

        ]
    },
    {
        id: 'TownHall',
        description: 'You are in the townhall',
        choices: [
            {
                id: 1,
                description: 'Go to bar',
                res_node: 'Bar'
            },
            {
                id: 2,
                description: 'Go to town center',
                res_node: 'TownCenter'
            },

        ]
    },{
        id: 'Bar',
        description: 'You are in the bar',
        choices: [
            {
                id: 1,
                description: 'Go to town center',
                res_node: 'TownCenter'
            },
            {
                id: 2,
                description: 'Go to townhall',
                res_node: 'TownHall'
            },

        ]
    },
]