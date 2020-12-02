using System.Collections.Generic;
using Xunit;

namespace Day1.Spec
{
    public class FindNumberTotals
    {
        [Fact]
        public void ReturnMultipleOf2ValuesThatAddto2020()
        {
            List<int> values = new List<int>() { 1000, 1020 };
            var solver = new Solver();
            var result = solver.Solve2(values);
            Assert.Equal(1020000, result);
        }

        [Fact]
        public void ReturnMultipleOf3ValuesThatAddto2020()
        {
            List<int> values = new List<int>() { 1721,
                979,
                366,
                299,
                675,
                1456 };
            var solver = new Solver();
            var result = solver.Solve3(values);
            Assert.Equal(241861950, result);
        }
    }
}
